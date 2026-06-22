def count_evens_bitwise(start, end):
    if start > end:
        return 0
    length = end - start + 1
    if length & 1:
        if start & 1:
            return length // 2
        return (length >> 1) + 1
    return length >> 1

if __name__ == '__main__':
    sample_start = 10
    sample_end = 20
    result = count_evens_bitwise(sample_start, sample_end)
    print(result)