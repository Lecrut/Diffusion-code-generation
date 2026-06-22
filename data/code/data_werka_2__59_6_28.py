def middle_element_generator(sequence):
    length = len(sequence)
    mid_index = length // 2
    
    if length % 2 == 1:
        yield sequence[mid_index]
    else:
        yield sequence[mid_index - 1]
        yield sequence[mid_index]

if __name__ == '__main__':
    sample_sequence_odd = [7, 8, 9, 10, 11]
    sample_sequence_even = [7, 8, 9, 10, 11, 12]
    
    print("Middle elements of odd-length sequence:")
    for middle in middle_element_generator(sample_sequence_odd):
        print(middle)
    
    print("Middle elements of even-length sequence:")
    for middle in middle_element_generator(sample_sequence_even):
        print(middle)