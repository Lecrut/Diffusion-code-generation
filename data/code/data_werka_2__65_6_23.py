def get_element_at_position(lst, position):
    if not isinstance(position, int):
        raise ValueError("Position must be an integer")
    try:
        return lst[position]
    except IndexError:
        return 'Index out of range'

def test_get_element_at_position():
    assert get_element_at_position([1, 2, 3, 4, 5], 2) == 3
    assert get_element_at_position([1, 2, 3, 4, 5], 0) == 1
    assert get_element_at_position([1, 2, 3, 4, 5], 4) == 5
    assert get_element_at_position([1, 2, 3, 4, 5], -1) == 5
    assert get_element_at_position([1, 2, 3, 4, 5], 5) == 'Index out of range'
    assert get_element_at_position([1, 2, 3, 4, 5], -6) == 'Index out of range'
    try:
        get_element_at_position([1, 2, 3, 4, 5], 'a')
    except ValueError as e:
        assert str(e) == "Position must be an integer"

if __name__ == '__main__':
    test_get_element_at_position()
    sample_list = [10, 20, 30, 40, 50]
    position = 2
    result = get_element_at_position(sample_list, position)
    print(result)