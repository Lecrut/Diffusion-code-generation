def middle_element_generator(sequence):
    length = len(sequence)
    if length % 2 == 0:
        mid_index1 = length // 2 - 1
        mid_index2 = length // 2
        yield sequence[mid_index1]
        yield sequence[mid_index2]
    else:
        mid_index = length // 2
        yield sequence[mid_index]

if __name__ == '__main__':
    sample_sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for middle in middle_element_generator(sample_sequence):
        print(middle)