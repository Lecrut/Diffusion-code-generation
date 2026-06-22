def get_element_at_position(lst, position):
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
if __name__ == '__main__':
    test_get_element_at_position()
    print(get_element_at_position([10, 20, 30, 40, 50], 2))