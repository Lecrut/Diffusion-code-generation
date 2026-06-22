def middle_element_generator(sequence):
    LENGTH_THRESHOLD = 1
    
    if len(sequence) < LENGTH_THRESHOLD:
        raise ValueError("The sequence is too short to have a middle element")
    
    mid_index = len(sequence) // 2
    
    if len(sequence) % 2 == 1:
        yield sequence[mid_index]
    else:
        yield sequence[mid_index - 1]
        yield sequence[mid_index]

if __name__ == '__main__':
    sample_sequence_odd = [10, 20, 30, 40, 50]
    sample_sequence_even = [10, 20, 30, 40, 50, 60]
    
    print("Middle elements of odd-length sequence:")
    for middle in middle_element_generator(sample_sequence_odd):
        print(middle)
    
    print("\nMiddle elements of even-length sequence:")
    for middle in middle_element_generator(sample_sequence_even):
        print(middle)