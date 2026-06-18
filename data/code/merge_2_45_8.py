import asyncio
async def sum_numbers(numbers: list[int]) -> int:
    return sum(numbers)
async def handle_request(user_id: str, numbers: list[int]) -> dict[str, any]:
    result = await asyncio.create_task(sum_numbers(numbers))
    return {"user": user_id, "sum": result}
async def main():
    requests = [
        ("alice", [1, 2, 3]),
        ("bob", [4, 5, 6]),
        ("charlie", [7, 8, 9]),
        ("diana", [10, 11]),
    ]
    tasks = [handle_request(user_id, nums) for user_id, nums in requests]
    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)
if __name__ == '__main__':
    asyncio.run(main())