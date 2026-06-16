import asyncio
class MockServer:
    def __init__(self, name, delay=0.1):
        self.name = name
        self.delay = delay
    async def fetch(self, data):
        await asyncio.sleep(self.delay)
        if isinstance(data, dict) and "error" in data.get("payload", {}):
            raise ConnectionError(f"{self.name} returned an error: {data['payload']['message']}")
        return {"status": "success", "server": self.name, "received_data": data["payload"]}
async def handle_request(server_name, payload):
    server = MockServer(server_name)
    try:
        result = await server.fetch(payload)
        print(f"[{server.name}] Success: {result}")
        return {"status_code": 200, "data": result}
    except ConnectionError as e:
        print(f"[{server.name}] Error: {e}")
        return {"status_code": 503, "error_message": str(e)}
async def main():
    tasks = [
        handle_request("Server-A", {"payload": {"id": 1}}),
        handle_request("Server-B", {"payload": {"id": 2}, "error": {"message": "Service Unavailable"}}),
        handle_request("Server-C", {"payload": {"id": 3, "timeout": True}})
    ]
    results = await asyncio.gather(*tasks)
    print("\nAll requests completed.")
if __name__ == '__main__':
    asyncio.run(main())