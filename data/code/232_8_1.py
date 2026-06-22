def generate_sequence(start, end):
    sequence = [0] * (end - start + 1)
    for i in range(start, end + 1):
        sequence[i - start] = i
    return sequence

if __name__ == '__main__':
    sample_start = 5
    sample_end = 10
    result = generate_sequence(sample_start, sample_end)
    print(result)