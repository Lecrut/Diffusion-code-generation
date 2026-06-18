import asyncio
async def sort_numbers(numbers: list) -> tuple[list]:
    return sorted(numbers), numbers
async def main():
    data = [54321, 98765, 11111]
    results = await asyncio.gather(sort_numbers(data))
if __name__ == '__main__':
    asyncio.run(main())