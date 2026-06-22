def count_even_numbers(start: int, end: int) -> int:
    if start > end:
        return 0
    first_even = start + (start % 2)
    if first_even > end:
        return 0
    last_even = end - (end % 2)
    return (last_even - first_even) // 2 + 1

if __name__ == '__main__':
    result = count_even_numbers(1, 10)
    print(result)
    result = count_even_numbers(5, 15)
    print(result)
    result = count_even_numbers(2, 2)
    print(result)
    result = count_even_numbers(3, 3)
    print(result)
    result = count_even_numbers(1, 1)
    print(result)
    result = count_even_numbers(10, 5)
    print(result)