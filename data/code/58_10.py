def count_even_in_range(start: int, end: int) -> int:
    if start > end:
        return 0
    return (end // 2) - ((start - 1) // 2)

if __name__ == '__main__':
    print(count_even_in_range(1, 10))
    print(count_even_in_range(5, 15))
    print(count_even_in_range(0, 0))
    print(count_even_in_range(-5, 5))
    print(count_even_in_range(10, 1))