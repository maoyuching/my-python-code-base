import asyncio
import asyncssh

import sys


async def run_client():
    async with asyncssh.connect('47.111.1.103', username='root', password='Maoyuqing@19971225') as conn:
        res_scp = await asyncssh.scp('C:/User/207325/Downloads/web-zy.zip', (conn,"web-zy.zip"))
        res = await conn.run('unzip -fo web-zy.zip', check=False)
        print(res.stdout if res.stdout else res.stderr, end='')


if __name__ == '__main__':
    try:
        asyncio.get_event_loop().run_until_complete(run_client())
    except(OSError, asyncssh.Error) as exc:
        # asyncssh.Error.args
        sys.exit("SSH connection failed" + str(exc))
