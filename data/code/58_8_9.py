def count_even_numbers(start: int, end: int) -> int:
    if start > end:
        start, end = end, start
    count = (end - start) // 2 + 1
    if start % 2 != 0:
        count -= 1
    return count

if __name__ == '__main__':
    start = 10
    end = 20
    result = count_even_numbers(start, end)
    print(result)