def middle_element_generator(sequence):
    length = len(sequence)
    if length == 0:
        raise ValueError("The sequence is empty")
    
    mid_index = length // 2
    
    if length % 2 == 1:
        yield sequence[mid_index]
    else:
        yield sequence[mid_index - 1]
        yield sequence[mid_index]

if __name__ == '__main__':
    sample_sequence_odd = [7, 8, 9, 10, 11]
    sample_sequence_even = [12, 13, 14, 15, 16, 17]
    
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