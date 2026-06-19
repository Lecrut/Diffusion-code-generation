def get_first_element(lst):
    return lst[0]

if __name__ == '__main__':
    int_list = [1, 2, 3]
    str_list = ['apple', 'banana', 'cherry']
    float_list = [1.1, 2.2, 3.3]
    mixed_list = [1, 'two', 3.0]

    assert get_first_element(int_list) == 1
    assert get_first_element(str_list) == 'apple'
    assert get_first_element(float_list) == 1.1
    assert get_first_element(mixed_list) == 1

    print(get_first_element(int_list))
    print(get_first_element(str_list))
    print(get_first_element(float_list))
    print(get_first_element(mixed_list))