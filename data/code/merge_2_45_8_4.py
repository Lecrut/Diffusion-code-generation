import asyncio
async def process_sum(value: int) -> int:
    await asyncio.sleep(0.1)
    return value * 2
async def main():
    tasks = [process_sum(i) for i in range(5)]
    results = await asyncio.gather(*tasks)
    print(results)
if __name__ == '__main__':
    asyncio.run(main())