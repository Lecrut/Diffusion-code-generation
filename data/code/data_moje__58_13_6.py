def count_even_numbers_in_range(start, end):
    if start > end:
        start, end = end, start

    first_even = start + (1 if start % 2 != 0 else 0)
    last_even = end - (1 if end % 2 != 0 else 0)

    if first_even > last_even:
        return 0

    return (last_even - first_even) // 2 + 1

if __name__ == '__main__':
    sample_start = 1
    sample_end = 10
    result = count_even_numbers_in_range(sample_start, sample_end)
    print(result)

    sample_start_2 = 5
    sample_end_2 = 15
    result_2 = count_even_numbers_in_range(sample_start_2, sample_end_2)
    print(result_2)

    sample_start_3 = 2
    sample_end_3 = 2
    result_3 = count_even_numbers_in_range(sample_start_3, sample_end_3)
    print(result_3)

    sample_start_4 = 3
    sample_end_4 = 3
    result_4 = count_even_numbers_in_range(sample_start_4, sample_end_4)
    print(result_4)