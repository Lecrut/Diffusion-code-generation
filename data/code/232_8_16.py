def growing_sequence(start, end):
    sequence = [start]
    for i in range(1, end - start + 1):
        sequence.append(sequence[-1] + i)
    return sequence

if __name__ == '__main__':
    sample_start = 5
    sample_end = 10
    result = growing_sequence(sample_start, sample_end)
    print(result)