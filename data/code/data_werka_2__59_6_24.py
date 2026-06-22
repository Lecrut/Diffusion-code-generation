def middle_element_generator(sequence):
    length = len(sequence)
    if length == 0:
        return
    mid_index = length // 2
    yield sequence[mid_index]

if __name__ == '__main__':
    sample_sequence = [1, 2, 3, 4, 5]
    for middle in middle_element_generator(sample_sequence):
        print(middle)