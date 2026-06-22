def count_evens(start, end):
    if start > end:
        return 0
    first_even = start if start % 2 == 0 else start + 1
    if first_even > end:
        return 0
    last_even = end if end % 2 == 0 else end - 1
    return (last_even - first_even) // 2 + 1

if __name__ == '__main__':
    sample_start = 10
    sample_end = 20
    print(count_evens(sample_start, sample_end))
    sample_start = 3
    sample_end = 7
    print(count_evens(sample_start, sample_end))
    sample_start = 5
    sample_end = 5
    print(count_evens(sample_start, sample_end))