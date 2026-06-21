def middle_element_generator(sequence):
    if not sequence:
        raise ValueError("The sequence is empty")
    
    length = len(sequence)
    mid_index = length // 2
    
    if length % 2 == 1:
        yield sequence[mid_index]
    else:
        yield sequence[mid_index - 1]
        yield sequence[mid_index]

if __name__ == '__main__':
    sample_sequence_odd = [10, 20, 30, 40, 50]
    sample_sequence_even = [10, 20, 30, 40, 50, 60]
    
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