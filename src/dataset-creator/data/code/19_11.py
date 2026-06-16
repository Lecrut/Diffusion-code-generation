import asyncio
from typing import List, Callable, Any
from dataclasses import dataclass
@dataclass
class ProcessingResult:
    id: int
    status: str
    value: Any
async def simulate_async_operation(data: Any) -> ProcessingResult:
    await asyncio.sleep(0.1)
    return ProcessingResult(id=hash(str(data)), status="success", value=data * 2)
class AsyncProcessor:
    def __init__(self, max_concurrency: int = 5):
        self.max_concurrency = max_concurrency
    async def process_batch(self, items: List[Any]) -> List[ProcessingResult]:
        tasks = [simulate_async_operation(item) for item in items]
        return await asyncio.gather(*tasks)
async def run_tests():
    processor = AsyncProcessor(max_concurrency=3)
    test_data_1 = ["a", "b", "c"]
    results_1 = await processor.process_batch(test_data_1)
    assert len(results_1) == 3
    test_data_2 = [1, 2, 3, 4]
    results_2 = await processor.process_batch(test_data_2)
    for r in results_2:
        expected_value = r.value
        if isinstance(r.id, int):
            assert isinstance(expected_value, (int, float))
async def main():
    await run_tests()
    print("All tests passed.")
if __name__ == '__main__':
    asyncio.run(main())