def find_middle_generator(sequence):
    n = len(sequence)
    if n == 0:
        raise ValueError("Sequence cannot be empty")
    middle_index = n // 2
    yield sequence[middle_index]

if __name__ == '__main__':
    sample_sequence_odd = [1, 2, 3, 4, 5]
    sample_sequence_even = [10, 20, 30, 40, 50, 60]
    
    for middle_element in find_middle_generator(sample_sequence_odd):
        print(f"Middle element of odd sequence: {middle_element}")
    
    for middle_element in find_middle_generator(sample_sequence_even):
        print(f"Middle element of even sequence: {middle_element}")