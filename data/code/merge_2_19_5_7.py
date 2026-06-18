import asyncio
from typing import List, Tuple
class MockServer:
    def __init__(self, name: str, delay: float):
        self.name = name
        self.delay = delay
    async def request(self) -> Tuple[str, bool]:
        await asyncio.sleep(self.delay)
        if random.random() < 0.3:
            return f"Error from {self.name}", False
        return f"Success from {self.name}", True
async def fetch_data(server_name: str) -> List[Tuple[str, bool]]:
    servers = [MockServer(f"{server_name}_A", 1), MockServer(f"{server_name}_B", 0.5)]
    tasks = []
    for server in servers:
        task = asyncio.create_task(server.request())
        tasks.append(task)
    results = await asyncio.gather(*tasks, return_exceptions=True)
    processed_results = []
    for result in results:
        if isinstance(result, Exception):
            continue
        status_name, is_success = result
        processed_results.append((status_name, is_success))
        print(f"Processed {server.name}: Status={is_success}")
    return processed_results
async def main():
    targets = ["Service1", "Service2"]
    for target in targets:
        await fetch_data(target)
if __name__ == '__main__':
    import random
    asyncio.run(main())