def count_even_in_range(start, end):
    if start > end:
        start, end = end, start
    first_even = start + (start % 2)
    if first_even > end:
        return 0
    last_even = end - (end % 2)
    count = (last_even - first_even) // 2 + 1
    return count

if __name__ == '__main__':
    print(count_even_in_range(1, 10))
    print(count_even_in_range(-5, 5))
    print(count_even_in_range(2, 2))
    print(count_even_in_range(3, 3))
    print(count_even_in_range(10, 1))
    print(count_even_in_range(-10, -1))
    print(count_even_in_range(0, 0))
    print(count_even_in_range(-7, -7))