def get_middle_element(sequence):
    if not sequence:
        raise ValueError("Sequence must not be empty")
    middle_index = len(sequence) // 2
    return sequence[middle_index]

if __name__ == '__main__':
    assert get_middle_element([1, 2, 3]) == 2
    assert get_middle_element([1, 2, 3, 4]) == 2
    assert get_middle_element([1, 2, 3, 4, 5]) == 3
    assert get_middle_element([1]) == 1
    assert get_middle_element([10, 20]) == 10
    print(get_middle_element([1, 2, 3, 4, 5]))
    print(get_middle_element([7, 8, 9]))
    print(get_middle_element([42]))