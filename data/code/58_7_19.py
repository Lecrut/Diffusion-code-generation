def count_even_in_range(start, end):
    if start > end:
        start, end = end, start
    first_even = start if start % 2 == 0 else start + 1
    last_even = end if end % 2 == 0 else end - 1
    if first_even > last_even:
        return 0
    return (last_even - first_even) // 2 + 1

if __name__ == '__main__':
    print(count_even_in_range(1, 10))
    print(count_even_in_range(-5, 5))
    print(count_even_in_range(7, 7))
    print(count_even_in_range(2, 2))
    print(count_even_in_range(3, 3))
    print(count_even_in_range(0, 0))
    print(count_even_in_range(-10, -1))
    print(count_even_in_range(1, 1))
    print(count_even_in_range(-3, -3))
    print(count_even_in_range(10, 1))