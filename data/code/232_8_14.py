def growing_sequence(start, end):
    seq = [0] * (end - start + 1)
    for i in range(start, end + 1):
        seq[i - start] = i
    return seq

if __name__ == '__main__':
    sample_start = 5
    sample_end = 10
    result = growing_sequence(sample_start, sample_end)
    print(result)