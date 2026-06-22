def find_middle_index(sequence):
    length = len(sequence)
    middle_index = (length - 1) // 2
    return middle_index

if __name__ == '__main__':
    sample_sequences = {
        'odd': [1, 2, 3, 4, 5],
        'even': [1, 2, 3, 4, 5, 6]
    }
    
    for key, sequence in sample_sequences.items():
        middle_index = find_middle_index(sequence)
        print(f"Middle index of {key} sequence: {middle_index}")