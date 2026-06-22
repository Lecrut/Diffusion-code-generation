def count_even_numbers(start, end):
    if start > end:
        return 0
    first_even = start + (1 if start % 2 != 0 else 0)
    last_even = end - (1 if end % 2 != 0 else 0)
    if first_even > last_even:
        return 0
    return (last_even - first_even) // 2 + 1

if __name__ == '__main__':
    print(count_even_numbers(1, 10))
    print(count_even_numbers(5, 15))
    print(count_even_numbers(2, 2))
    print(count_even_numbers(3, 3))
    print(count_even_numbers(-5, 5))