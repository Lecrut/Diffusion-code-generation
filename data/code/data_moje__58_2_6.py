def count_even_numbers(start, end):
    if start > end:
        return 0
    total = end - start + 1
    start_is_even = not start & 1
    if start_is_even:
        return total + 1 >> 1
    else:
        return total >> 1
if __name__ == '__main__':
    sample_start = 1
    sample_end = 10
    result = count_even_numbers(sample_start, sample_end)
    print(result)