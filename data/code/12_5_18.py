def get_middle_element(sequence):
    mid_index = len(sequence) // 2
    return sequence[mid_index]

if __name__ == '__main__':
    assert get_middle_element([1, 2, 3]) == 2
    assert get_middle_element([1, 2, 3, 4, 5]) == 3
    assert get_middle_element(['a', 'b', 'c', 'd']) == 'c'
    assert get_middle_element([10]) == 10
    print(get_middle_element([4, 7, 1, 9, 2]))