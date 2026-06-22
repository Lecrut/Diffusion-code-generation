def count_even_numbers(start, end):
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("start and end must be integers")
    if start > end:
        return 0
    first_even = start if start % 2 == 0 else start + 1
    if first_even > end:
        return 0
    last_even = end if end % 2 == 0 else end - 1
    return (last_even - first_even) // 2 + 1

if __name__ == '__main__':
    print(count_even_numbers(1, 10))
    print(count_even_numbers(2, 10))
    print(count_even_numbers(5, 5))
    print(count_even_numbers(6, 6))
    print(count_even_numbers(7, 7))
    print(count_even_numbers(10, 1))