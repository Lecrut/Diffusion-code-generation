import asyncio
async def sort_numbers(numbers: list) -> tuple[list]:
    return sorted(numbers), numbers
async def main():
    data = [54321, 98765, 11111, 50000]
    result_list = await asyncio.gather(*[sort_numbers(data.copy()) for _ in range(1)])
    return result_list
if __name__ == '__main__':
    print(asyncio.run(main()))