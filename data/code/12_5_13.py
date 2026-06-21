def get_middle_element(seq):
    if len(seq) == 0:
        raise ValueError("Sequence cannot be empty")
    return seq[len(seq) // 2]

if __name__ == '__main__':
    test_list = [1, 2, 3, 4, 5]
    print(get_middle_element(test_list))
    assert get_middle_element(test_list) == 3
    test_tuple = (10, 20, 30, 40, 50, 60)
    print(get_middle_element(test_tuple))
    assert get_middle_element(test_tuple) == 40
    test_str = "abcdefg"
    print(get_middle_element(test_str))
    assert get_middle_element(test_str) == 'd'