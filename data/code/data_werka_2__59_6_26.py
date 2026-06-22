def is_sequence_empty(sequence):
    return len(sequence) == 0

def has_single_middle_element(sequence):
    return len(sequence) % 2 == 1

def middle_element_generator(sequence):
    if is_sequence_empty(sequence):
        raise ValueError("The sequence is empty")
    
    length = len(sequence)
    mid_index = length // 2
    
    if has_single_middle_element(sequence):
        yield sequence[mid_index]
    else:
        yield sequence[mid_index - 1]
        yield sequence[mid_index]

if __name__ == '__main__':
    sample_sequence_odd = [7, 8, 9, 10, 11]
    sample_sequence_even = [2, 4, 6, 8, 10, 12]
    
    print("Middle elements of odd-length sequence:")
    try:
        for middle in middle_element_generator(sample_sequence_odd):
            print(middle)
    except ValueError as e:
        print(e)
    
    print("\nMiddle elements of even-length sequence:")
    try:
        for middle in middle_element_generator(sample_sequence_even):
            print(middle)
    except ValueError as e:
        print(e)