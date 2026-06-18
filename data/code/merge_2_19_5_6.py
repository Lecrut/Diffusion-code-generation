import asyncio
class MockServer:
    def __init__(self, name, delay=0.1):
        self.name = name
        self.delay = delay
    async def request(self, data):
        await asyncio.sleep(self.delay)
        if isinstance(data, str):
            return f"Success from {self.name}: {data}"
        elif isinstance(data, int):
            result = data * 2
            if result > 10:
                raise ValueError(f"Value too large for server {self.name}")
            return {"status": "ok", "result": result}
        return f"Success from {self.name}: Unknown type handled as string"
async def fetch_data(server, data):
    try:
        response = await server.request(data)
        print(f"[{server.name}] Received: {response}")
        return True, None
    except Exception as e:
        error_msg = f"{type(e).__name__}: {e}"
        print(f"[{server.name}] Error: {error_msg}")
        return False, str(e)
async def main():
    servers = [MockServer("Alpha", 0.2), MockServer("Beta", 0.3)]
    tasks = []
    for server in servers:
        task = asyncio.create_task(fetch_data(server, "Hello"))
        tasks.append(task)
    results = await asyncio.gather(*tasks)
    success_count = sum(1 for r in results if r[0])
    print(f"\nTotal requests completed successfully: {success_count}/{len(results)}")
if __name__ == '__main__':
    main()