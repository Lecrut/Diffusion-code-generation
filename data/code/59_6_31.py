def is_odd(n):
    return n % 2 == 1

def middle_element_generator(sequence):
    length = len(sequence)
    
    if not sequence:
        raise ValueError("The sequence is empty")
    
    mid_index = length // 2
    
    if is_odd(length):
        yield sequence[mid_index]
    else:
        yield sequence[mid_index - 1]
        yield sequence[mid_index]

if __name__ == '__main__':
    sample_sequence_odd = [1, 2, 3, 4, 5]
    sample_sequence_even = [1, 2, 3, 4, 5, 6]
    
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