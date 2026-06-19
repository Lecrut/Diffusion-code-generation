def middle_element_generator(sequence):
    length = len(sequence)
    mid_index = length // 2
    if length % 2 == 0:
        yield sequence[mid_index - 1]
    yield sequence[mid_index]

if __name__ == '__main__':
    sample_sequence = [1, 2, 3, 4, 5, 6]
    for element in middle_element_generator(sample_sequence):
        print(element)