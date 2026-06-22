def average_of_sequences(sequences):
    if not sequences:
        return 0.0
    total_sum = 0.0
    element_count = 0
    for seq in sequences:
        if not all(isinstance(x, (int, float)) for x in seq):
            raise ValueError("All elements in each sequence must be numbers.")
        total_sum += sum(seq)
        element_count += len(seq)
    if element_count == 0:
        return 0.0
    else:
        return total_sum / element_count

if __name__ == '__main__':
    sequences_sample = [
        [1, 2, 3],
        [4.5, 6.7],
        [-1, -2]
    ]
    result = average_of_sequences(sequences_sample)
    print(result)