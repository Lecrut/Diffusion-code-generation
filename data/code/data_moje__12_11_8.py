def find_middle_element(sequence):
    if not sequence:
        raise ValueError("Empty sequence has no middle element")
    if not isinstance(sequence, tuple):
        raise TypeError("Input must be a tuple")
    mid_index = len(sequence) // 2
    return sequence[mid_index]

if __name__ == '__main__':
    sample_tuple = (1, 2, 3, 4, 5)
    print(find_middle_element(sample_tuple))
    sample_tuple_even = (1, 2, 3, 4)
    print(find_middle_element(sample_tuple_even))
    try:
        find_middle_element(())
    except ValueError as e:
        print(e)