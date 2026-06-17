import asyncio
from concurrent.futures import ThreadPoolExecutor
import random
def verify_name(name: str) -> bool:
    return len(name.strip()) > 0 and not any(c.isdigit() for c in name.lower()) if name else False
async def process_single_task(index: int, names_list: list[str]) -> dict[int, tuple[str, bool]]:
    await asyncio.sleep(0.1)                            
    return index, (names_list[index], verify_name(names_list[index]))
async def bulk_verify_concurrent(num_names: int = 5):
    names = [f"User_{i}" for i in range(num_names)]
    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor(max_workers=4) as executor:
        tasks = []
        for idx, name in enumerate(names):
            tasks.append(loop.run_in_executor(executor, process_single_task, idx, names))
        results = await asyncio.gather(*tasks)
    return {idx: data for idx, (name, is_valid) in zip(results[0], results)}
if __name__ == '__main__':
    result_map = bulk_verify_concurrent(num_names=10)
    print(result_map)