import asyncio
async def process_sum(value: int) -> int:
    await asyncio.sleep(0.1)
    return value * 2 + sum(range(1, value))
if __name__ == '__main__':
    tasks = [process_sum(i) for i in range(5)]
    results = asyncio.gather(*tasks)
    print(results)