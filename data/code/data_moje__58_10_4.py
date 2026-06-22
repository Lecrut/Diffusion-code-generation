def count_even_numbers(start, end):
    if start > end:
        return 0
    first_even = start + (start % 2 != 0)
    if first_even > end:
        return 0
    last_even = end - (end % 2 != 0)
    return (last_even - first_even) // 2 + 1

if __name__ == '__main__':
    print(count_even_numbers(1, 10))
    print(count_even_numbers(2, 8))
    print(count_even_numbers(3, 7))
    print(count_even_numbers(10, 10))
    print(count_even_numbers(5, 5))