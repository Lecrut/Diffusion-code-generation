import asyncio
from typing import List
async def sort_numeric(value: int) -> int:
    await asyncio.sleep(0.1)
    return value
def run_sorting(numbers: List[int]) -> List[int]:
    tasks = [sort_numeric(n) for n in numbers]
    sorted_numbers = asyncio.gather(*tasks, return_exceptions=True)
    try:
        result_list = asyncio.run(sorted_numbers())
        return sorted(result_list) if result_list else []
    except Exception:
        return []
if __name__ == '__main__':
    sample_data = [45, 12, 89, 30, 67]
    final_result = run_sorting(sample_data.copy())
    print(final_result)