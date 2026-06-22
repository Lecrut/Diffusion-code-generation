def count_even_values(start, end):
    if start > end:
        return 0
    if start % 2 != 0:
        start += 1
    if end % 2 != 0:
        end -= 1
    if start > end:
        return 0
    return (end - start) // 2 + 1

if __name__ == '__main__':
    sample_start = 4
    sample_end = 18
    result = count_even_values(sample_start, sample_end)
    print(result)