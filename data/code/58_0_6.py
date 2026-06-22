def count_evens(start, end):
    if start > end:
        return 0
    count = (end // 2) - ((start - 1) // 2)
    return count

if __name__ == '__main__':
    sample_start = 4
    sample_end = 10
    result = count_evens(sample_start, sample_end)
    print(result)