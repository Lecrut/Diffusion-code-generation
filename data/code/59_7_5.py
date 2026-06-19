def middle_element_generator(sequence):
    length = len(sequence)
    if length % 2 == 0:
        mid_index = length // 2 - 1
        yield sequence[mid_index]
        yield sequence[mid_index + 1]
    else:
        mid_index = length // 2
        yield sequence[mid_index]

if __name__ == '__main__':
    sample_sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for middle in middle_element_generator(sample_sequence):
        print(middle)