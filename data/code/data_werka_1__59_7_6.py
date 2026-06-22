def find_middle(sequence):
    n = len(sequence)
    if n == 0:
        raise ValueError('Sequence cannot be empty')
    middle_index = n // 2
    return sequence[middle_index]
if __name__ == '__main__':
    sample_sequence_1 = [5, 10, 15, 20, 25]
    sample_sequence_2 = ['a', 'b', 'c', 'd', 'e', 'f']
    middle_element_1 = find_middle(sample_sequence_1)
    middle_element_2 = find_middle(sample_sequence_2)
    print(middle_element_1)
    print(middle_element_2)