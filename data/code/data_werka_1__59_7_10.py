def find_middle(sequence):
    n = len(sequence)
    if n == 0:
        raise ValueError("Sequence cannot be empty")
    middle_index = n // 2
    yield sequence[middle_index]

if __name__ == '__main__':
    sample_sequences = [
        [1, 2, 3, 4, 5],
        [10, 20, 30, 40, 50, 60, 70],
        [1, 2, 3, 4],
        [10, 20, 30, 40, 50]
    ]
    
    for seq in sample_sequences:
        middle_value = next(find_middle(seq))
        print(middle_value)