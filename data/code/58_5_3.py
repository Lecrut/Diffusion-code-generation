def count_evens(start, end):
    count = 0
    current = start
    if current > end:
        return 0
    if current % 2 == 1:
        current += 1
    while current <= end:
        count += 1
        current += 2
    return count

if __name__ == '__main__':
    sample_start = 10
    sample_end = 25
    result = count_evens(sample_start, sample_end)
    print(result)