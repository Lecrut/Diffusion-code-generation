def get_middle_element(sequence):
    if not sequence:
        raise ValueError("Sequence is empty")
    mid_index = len(sequence) // 2
    return sequence[mid_index]

if __name__ == '__main__':
    assert get_middle_element([1, 2, 3]) == 2
    assert get_middle_element([1, 2, 3, 4]) == 2
    assert get_middle_element([5]) == 5
    assert get_middle_element([1, 2, 3, 4, 5, 6, 7]) == 4
    print(get_middle_element([1, 2, 3, 4, 5]))