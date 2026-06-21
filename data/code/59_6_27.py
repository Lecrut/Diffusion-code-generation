def middle_element_generator(sequence):
    length = len(sequence)
    if length % 2 == 1:
        yield sequence[length // 2]
    else:
        yield sequence[length // 2 - 1]
        yield sequence[length // 2]

if __name__ == '__main__':
    sample_sequence = [1, 2, 3, 4, 5]
    for middle in middle_element_generator(sample_sequence):
        print(middle)