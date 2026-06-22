def find_middle_index(sequence):
    length = len(sequence)
    middle_index = (length - 1) // 2
    return middle_index

if __name__ == '__main__':
    sample_sequences = {
        'odd': [1, 2, 3, 4, 5],
        'even': [1, 2, 3, 4, 5, 6],
        'single': [7],
        'pair': [8, 9]
    }
    
    for key, sequence in sample_sequences.items():
        print(f"Middle index of {key} sequence: {find_middle_index(sequence)}")