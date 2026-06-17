import asyncio
async def sum_numbers(numbers: list[int]) -> int:
    return sum(numbers)
async def process_request(user_id: str, numbers: list[int]) -> dict[str, any]:
    result = await asyncio.create_task(sum_numbers(numbers))
    return {"user": user_id, "result": result}
async def main():
    tasks = [
        process_request("alice", [1, 2, 3]),
        process_request("bob", [4, 5, 6]),
        process_request("charlie", [7, 8, 9]),
    ]
    results = await asyncio.gather(*tasks)
    for r in results:
        print(r)
if __name__ == '__main__':
    asyncio.run(main())