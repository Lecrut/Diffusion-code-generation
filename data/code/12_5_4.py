def middle_element(sequence):
    if not sequence:
        raise ValueError("Sequence is empty")
    mid_index = len(sequence) // 2
    return sequence[mid_index]

if __name__ == '__main__':
    assert middle_element([1, 2, 3]) == 2
    assert middle_element([4, 5]) == 4
    assert middle_element([7]) == 7
    assert middle_element([1, 2, 3, 4, 5]) == 3
    print(middle_element([10, 20, 30, 40, 50]))
    print(middle_element([1, 2]))
    print(middle_element([99]))