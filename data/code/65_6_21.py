def get_element_at_position(lst, position):
    if not isinstance(position, int):
        raise ValueError("Position must be an integer")
    try:
        return lst[position]
    except IndexError:
        return "Index out of range"

def test_get_element_at_position():
    assert get_element_at_position([10, 20, 30, 40, 50], 2) == 30
    assert get_element_at_position([10, 20, 30, 40, 50], 0) == 10
    assert get_element_at_position([10, 20, 30, 40, 50], -1) == 50
    assert get_element_at_position([10, 20, 30, 40, 50], 4) == 50
    assert get_element_at_position([10, 20, 30, 40, 50], 5) == "Index out of range"
    assert get_element_at_position([10, 20, 30, 40, 50], -6) == "Index out of range"

if __name__ == '__main__':
    test_get_element_at_position()
    sample_list = [100, 200, 300, 400, 500]
    target_position = 2
    print(get_element_at_position(sample_list, target_position))