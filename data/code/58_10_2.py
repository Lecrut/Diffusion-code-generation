def count_even_numbers(start, end):
    if start > end:
        return 0
    total_numbers = end - start + 1
    if total_numbers % 2 == 0:
        return total_numbers // 2
    if start % 2 == 0:
        return (total_numbers // 2) + 1
    return total_numbers // 2

if __name__ == '__main__':
    sample_start = 3
    sample_end = 10
    result = count_even_numbers(sample_start, sample_end)
    print(result)