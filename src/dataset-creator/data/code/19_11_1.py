import asyncio
from typing import List, Callable, Any
from dataclasses import dataclass
@dataclass
class AsyncProcessor:
    def __init__(self, max_workers: int = 4):
        self.max_workers = max_workers
        self._loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self._loop)
    async def process_batch(
        self, items: List[Any], task_fn: Callable[[Any], Any]
    ) -> List[Any]:
        tasks = [asyncio.create_task(task_fn(item)) for item in items]
        results = await asyncio.gather(*tasks)
        return results
    async def run(self, test_items: Any):
        self._loop.run_until_complete(asyncio.sleep(0.1))
if __name__ == '__main__':
    processor = AsyncProcessor(max_workers=4)
    sample_data = [f"item_{i}" for i in range(20)]
    async def mock_task(item: str):
        await asyncio.sleep(0.05)
        return f"{item}_processed"
    results = asyncio.run(processor.process_batch(sample_data, mock_task))
    print("Batch processing completed successfully.")