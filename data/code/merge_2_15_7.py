import asyncio
async def sort_task(numbers: list[int]) -> tuple[list[int], int]:
    start = asyncio.get_event_loop().time()
    numbers.sort()
    end = asyncio.get_event_loop().time()
    elapsed_ms = (end - start) * 1000
    return numbers, int(elapsed_ms)
async def main():
    data_sets = [
        list(range(50)),
        list(reversed(range(30))),
        [42] * 20 + list(range(1, 20)),
        [-10, -5, 0, 5, 10],
        range(100),
    ]
    tasks = [sort_task(data) for data in data_sets]
    results = await asyncio.gather(*tasks)
    print("Sorting completed successfully.")
if __name__ == '__main__':
    import re
    main()