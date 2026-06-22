def create_growing_sequence(start, end):
    sequence = [0] * (end - start + 1)
    for index, value in enumerate(range(start, end + 1), start=start):
        sequence[index - start] = value
    return sequence

if __name__ == '__main__':
    sample_start = 3
    sample_end = 9
    result = create_growing_sequence(sample_start, sample_end)
    print(result)