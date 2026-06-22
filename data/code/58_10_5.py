def count_even_numbers(start: int, end: int) -> int:
    if start > end:
        start, end = end, start
    return (end // 2) - ((start - 1) // 2)

if __name__ == '__main__':
    print(count_even_numbers(1, 10))
    print(count_even_numbers(3, 7))
    print(count_even_numbers(2, 2))
    print(count_even_numbers(100, 200))
    print(count_even_numbers(-5, 5))