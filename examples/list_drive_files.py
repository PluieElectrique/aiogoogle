#!/usr/bin/python3.7

'''
API explorer link:

* https://developers.google.com/apis-explorer/#p/drive/v3/drive.files.list

Scopes Required:

* https://www.googleapis.com/auth/drive
* https://www.googleapis.com/auth/drive.file
'''

import asyncio

from helpers import Aiogoogle, user_creds, client_creds


async def list_files():
    async with Aiogoogle(user_creds=user_creds, client_creds=client_creds) as aiogoogle:
        drive_v3 = await aiogoogle.discover("drive", "v3")
        res = await aiogoogle.as_user(drive_v3.files.list(), full_res=True)
    async for page in res:
        for file in page["files"]:
            print(f"{file.get('id')}: {file.get('name')}")


if __name__ == "__main__":
    asyncio.run(list_files())
