import math

def count_evens(start, end):
    if start > end:
        return 0
    first_even = start if start % 2 == 0 else start + 1
    last_even = end if end % 2 == 0 else end - 1
    if first_even > last_even:
        return 0
    return math.floor((last_even - first_even) / 2) + 1

if __name__ == '__main__':
    sample_start = 1
    sample_end = 10
    result = count_evens(sample_start, sample_end)
    print(result)