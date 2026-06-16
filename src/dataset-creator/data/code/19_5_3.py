import asyncio
class MockServer:
    def __init__(self, name, delay=1):
        self.name = name
        self.delay = delay
    async def fetch(self, data=None):
        await asyncio.sleep(self.delay)
        if isinstance(data, dict) and "error" in data.get("payload", {}):
            raise Exception(f"{self.name} returned an error: {data['payload']['message']}")
        return {"status": f"{self.name}_success", "delay_used": self.delay}
async def handle_request(server_name, payload_data=None):
    server = MockServer(name=server_name)
    try:
        result = await server.fetch(payload_data=payload_data)
        print(f"[{server_name}] Success: {result}")
        return {"status_code": 200, "data": result}
    except Exception as e:
        error_msg = str(e) if isinstance(e, Exception) else f"Unknown exception occurred."
        print(f"[{server_name}] Error: {error_msg}")
        return {"status_code": 500, "message": error_msg}
async def main():
    tasks = [
        handle_request("Server_A", payload_data={"payload": {}}),
        handle_request("Server_B", payload_data={"payload": {"error": "timeout"}}),
        handle_request("Server_C", payload_data=None)
    ]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    for task_result in results:
        if isinstance(task_result, Exception):
            print(f"Unhandled exception from a background task")
if __name__ == '__main__':
    main()