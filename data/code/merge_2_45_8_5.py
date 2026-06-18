import asyncio
async def process_sum(value: int) -> int:
    await asyncio.sleep(0.1)
    return value + 5
async def main():
    tasks = [process_sum(i * 2) for i in range(1, 6)]
    results = await asyncio.gather(*tasks)
    print(f"Results: {results}")
if __name__ == '__main__':
    asyncio.run(main())