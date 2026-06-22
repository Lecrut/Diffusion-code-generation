def find_middle_element(sequence):
    if not sequence:
        raise ValueError("Sequence must not be empty")
    middle_index = len(sequence) // 2
    return sequence[middle_index]

if __name__ == '__main__':
    sample_tuple = (1, 2, 3, 4, 5)
    result = find_middle_element(sample_tuple)
    print(result)