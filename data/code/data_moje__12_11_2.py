def find_middle_element(sequence):
    if not sequence:
        raise ValueError("Sequence cannot be empty")
    mid_index = len(sequence) // 2
    return sequence[mid_index]

if __name__ == '__main__':
    sample_tuple = (10, 20, 30, 40, 50)
    result = find_middle_element(sample_tuple)
    print(result)
    empty_tuple = ()
    try:
        find_middle_element(empty_tuple)
    except ValueError as e:
        print(e)