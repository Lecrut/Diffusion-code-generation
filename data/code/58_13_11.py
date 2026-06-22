def count_even_numbers(start: int, end: int) -> int:
    if start > end:
        return 0
    if start % 2 == 0:
        return (end - start) // 2 + 1
    return (end - start + 1) // 2

if __name__ == '__main__':
    print(count_even_numbers(1, 10))
    print(count_even_numbers(2, 10))
    print(count_even_numbers(1, 1))
    print(count_even_numbers(2, 2))
    print(count_even_numbers(10, 5))