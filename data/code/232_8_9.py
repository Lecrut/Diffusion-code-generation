def growing_sequence(start, end):
    seq = [start]
    for i in range(1, end - start + 1):
        seq.append(seq[-1] + i)
    return seq

if __name__ == '__main__':
    sample_start = 5
    sample_end = 10
    result = growing_sequence(sample_start, sample_end)
    print(result)