import asyncio
class MockServer:
    def __init__(self, name, delay=0.5):
        self.name = name
        self.delay = delay
    async def fetch(self, data):
        await asyncio.sleep(self.delay)
        if isinstance(data, str) and "error" in data.lower():
            raise ConnectionError(f"{self.name} returned an error for: {data}")
        return {"status": "success", "server": self.name, "received_data": data}
async def handle_request(server_name, request_data):
    server = MockServer(server_name)
    try:
        result = await server.fetch(request_data)
        print(f"[{request_data}] -> {result}")
        return {"success": True, "data": result}
    except ConnectionError as e:
        print(f"ERROR on [{request_data}]: {e}")
        return {"success": False, "error": str(e)}
async def main():
    tasks = [
        handle_request("Server-A", "Hello"),
        handle_request("Server-B", "World"),
        handle_request("Server-C", "Error Test"),
        handle_request("Server-D", "Data 123")
    ]
    results = await asyncio.gather(*tasks)
    print("\nAll requests completed.")
if __name__ == '__main__':
    asyncio.run(main())