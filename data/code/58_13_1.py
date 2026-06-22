def count_even_numbers(start, end):
    if start > end:
        return 0
    first_even = start if start % 2 == 0 else start + 1
    last_even = end if end % 2 == 0 else end - 1
    if first_even > last_even:
        return 0
    return (last_even - first_even) // 2 + 1

if __name__ == '__main__':
    sample_ranges = [(1, 10), (5, 15), (2, 2), (3, 3), (10, 1)]
    for start, end in sample_ranges:
        result = count_even_numbers(start, end)
        print(result)