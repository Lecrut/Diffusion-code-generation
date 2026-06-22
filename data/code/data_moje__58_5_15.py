def count_even_in_range(start, end):
    if start > end:
        return 0
    first_even = start + (1 if start % 2 != 0 else 0)
    last_even = end - (1 if end % 2 != 0 else 0)
    if first_even > last_even:
        return 0
    return (last_even - first_even) // 2 + 1

if __name__ == '__main__':
    print(count_even_in_range(1, 10))
    print(count_even_in_range(2, 8))
    print(count_even_in_range(1, 1))
    print(count_even_in_range(10, 1))
    print(count_even_in_range(0, 5))