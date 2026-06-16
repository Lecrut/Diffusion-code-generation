import asyncio
class MockServer:
    def __init__(self, name, delay=0.5):
        self.name = name
        self.delay = delay
    async def fetch(self, data=None):
        try:
            await asyncio.sleep(self.delay)
            return {"status": "success", "data": f"Response from {self.name}"}
        except Exception as e:
            raise RuntimeError(f"{self.name} failed: {str(e)}")
async def handle_request(server, data):
    try:
        response = await server.fetch(data)
        return {"server": server.name, "status": "success", "response": response}
    except Exception as e:
        error_msg = f"Error from {server.name}: {str(e)}"
        print(error_msg)
        return {"server": server.name, "status": "error", "message": error_msg}
async def main():
    servers = [MockServer("Alpha"), MockServer("Beta")]
    tasks = []
    for i in range(3):
        task = asyncio.create_task(handle_request(servers[i % len(servers)], f"Request-{i}"))
        tasks.append(task)
    results = await asyncio.gather(*tasks, return_exceptions=True)
    print("\n--- Final Results ---")
    for result in results:
        if isinstance(result, Exception):
            pass                                
        else:
            print(f"Result from {result['server']}: {result}")
if __name__ == '__main__':
    asyncio.run(main())