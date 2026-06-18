import asyncio
class MockServer:
    def __init__(self, name, delay=0.5):
        self.name = name
        self.delay = delay
    async def fetch(self, data):
        await asyncio.sleep(self.delay)
        if isinstance(data, str) and "error" in data.lower():
            raise ConnectionError(f"{self.name} returned an error for: {data}")
        return f"[{self.name}] Success with payload: {data}"
async def process_request(server_name, request_data):
    server = MockServer(server_name)
    try:
        result = await server.fetch(request_data)
        print(f"Completed successfully on {server_name}: {result}")
        return {"status": "success", "message": result}
    except ConnectionError as e:
        print(f"Failed on {server_name}: {e}")
        return {"status": "error", "message": str(e)}
async def main():
    tasks = [
        process_request("Server A", "normal_data"),
        process_request("Server B", "another_normal"),
        process_request("Server C", "trigger_error"),
        process_request("Server D", "final_task")
    ]
    results = await asyncio.gather(*tasks)
if __name__ == '__main__':
    main()