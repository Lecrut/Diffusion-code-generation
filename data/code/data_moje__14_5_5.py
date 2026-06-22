def get_third_item(sequence):
    if len(sequence) < 3:
        raise ValueError("Sequence must have at least three elements")
    return sequence[2]

if __name__ == '__main__':
    sample_sequence = [1, 2, 3, 4, 5]
    result = get_third_item(sample_sequence)
    print(result)