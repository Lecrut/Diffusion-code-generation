def middle_element_generator(sequence):
    length = len(sequence)
    mid_index = length // 2
    if length % 2 == 1:
        yield sequence[mid_index]
    else:
        yield sequence[mid_index - 1]
        yield sequence[mid_index]

if __name__ == '__main__':
    sample_sequences = {
        'odd': [1, 2, 3, 4, 5],
        'even': [10, 20, 30, 40, 50, 60]
    }
    
    for seq_type, sequence in sample_sequences.items():
        print(f"Middle elements of {seq_type} length sequence:")
        try:
            for middle in middle_element_generator(sequence):
                print(middle)
        except ValueError as e:
            print(e)