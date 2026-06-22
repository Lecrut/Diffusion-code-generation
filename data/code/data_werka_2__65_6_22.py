def get_element_at_position(lst, position):
    try:
        return lst[position]
    except IndexError:
        raise ValueError("Position out of range")

def test_get_element_at_position():
    assert get_element_at_position([1, 2, 3, 4, 5], 0) == 1
    assert get_element_at_position([1, 2, 3, 4, 5], 2) == 3
    assert get_element_at_position([1, 2, 3, 4, 5], 4) == 5
    try:
        get_element_at_position([1, 2, 3, 4, 5], 5)
    except ValueError as e:
        assert str(e) == "Position out of range"
    try:
        get_element_at_position([1, 2, 3, 4, 5], -1)
    except ValueError as e:
        assert str(e) == "Position out of range"

if __name__ == '__main__':
    test_get_element_at_position()