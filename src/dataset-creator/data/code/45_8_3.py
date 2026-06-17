import asyncio
async def process_sum(value: int) -> dict:
    return {"input": value, "sum": sum(range(10_000))}
async def main():
    tasks = [process_sum(i * 2 + 3) for i in range(5)]
    results = await asyncio.gather(*tasks)
    print(results)
if __name__ == '__main__':
    asyncio.run(main())