def growing_sequence(start, end):
    if not isinstance(start, int) or not isinstance(end, int):
        raise ValueError("Both start and end must be integers.")
    if start > end:
        raise ValueError("Start value must be less than or equal to end value.")

    sequence = [0] * (end - start + 1)
    for i in range(start, end + 1):
        sequence[i - start] = i
    return sequence

if __name__ == '__main__':
    sample_start = 5
    sample_end = 10
    result = growing_sequence(sample_start, sample_end)
    print(result)