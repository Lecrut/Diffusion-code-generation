def middle_element_generator(sequence):
    if not sequence:
        raise ValueError('Sequence cannot be empty')
    n = len(sequence)
    middle_index = n // 2
    yield sequence[middle_index]
if __name__ == '__main__':
    try:
        sample_sequence1 = [1, 2, 3, 4, 5]
        print(next(middle_element_generator(sample_sequence1)))
        sample_sequence2 = [10, 20, 30, 40, 50, 60, 70]
        print(next(middle_element_generator(sample_sequence2)))
        sample_sequence3 = []
        print(next(middle_element_generator(sample_sequence3)))
    except ValueError as e:
        print(e)