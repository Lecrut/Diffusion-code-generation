def middle_element_generator(sequence):
    length = len(sequence)
    if length % 2 == 1:
        mid_index = length // 2
        yield sequence[mid_index]
    else:
        raise ValueError("Sequence does not have a single middle element")

if __name__ == '__main__':
    sample_sequence = [1, 2, 3, 4, 5]
    try:
        for middle in middle_element_generator(sample_sequence):
            print(middle)
    except ValueError as e:
        print(e)

    sample_even_sequence = [1, 2, 3, 4]
    try:
        for middle in middle_element_generator(sample_even_sequence):
            print(middle)
    except ValueError as e:
        print(e)