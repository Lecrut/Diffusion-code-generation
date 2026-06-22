def count_even_numbers(start, end):
    if start > end:
        return 0
    total_numbers = end - start + 1
    if total_numbers == 0:
        return 0
    count = total_numbers // 2
    if total_numbers % 2 == 1:
        if start & 1 == 0:
            count += 1
        elif end & 1 == 0:
            count += 1
    return count
if __name__ == '__main__':
    sample_start = 1
    sample_end = 10
    result = count_even_numbers(sample_start, sample_end)
    print(result)