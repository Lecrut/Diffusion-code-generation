def get_element_at_position(lst, position):
    try:
        return lst[position]
    except IndexError:
        raise ValueError('Position out of range')

def test_get_element_at_position():
    sample_list = [10, 20, 30, 40, 50]
    assert get_element_at_position(sample_list, 0) == 10
    assert get_element_at_position(sample_list, 2) == 30
    assert get_element_at_position(sample_list, 4) == 50
    try:
        get_element_at_position(sample_list, 5)
    except ValueError as e:
        assert str(e) == 'Position out of range'
    try:
        get_element_at_position(sample_list, -6)
    except ValueError as e:
        assert str(e) == 'Position out of range'
if __name__ == '__main__':
    test_get_element_at_position()