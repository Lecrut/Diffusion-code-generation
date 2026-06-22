def count_even_numbers(start, end):
    if start > end:
        return 0
    if start % 2 == 0:
        first_even = start
    else:
        first_even = start + 1
    if end % 2 == 0:
        last_even = end
    else:
        last_even = end - 1
    if first_even > last_even:
        return 0
    return (last_even - first_even) // 2 + 1

if __name__ == '__main__':
    print(count_even_numbers(1, 10))
    print(count_even_numbers(2, 10))
    print(count_even_numbers(1, 1))
    print(count_even_numbers(5, 5))
    print(count_even_numbers(-5, 5))
    print(count_even_numbers(10, 1))