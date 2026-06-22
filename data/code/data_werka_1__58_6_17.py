def access_first_element(data):
    return data[0]
if __name__ == '__main__':
    integer_list = [42, 84, 168]
    string_list = ['hello', 'world', 'python']
    float_list = [3.14159, 2.71828, 1.41421]
    boolean_list = [True, False, True]
    int_first_element = access_first_element(integer_list)
    assert int_first_element == 42
    print(f'First element of integer_list: {int_first_element}')
    string_first_element = access_first_element(string_list)
    assert string_first_element == 'hello'
    print(f'First element of string_list: {string_first_element}')
    float_first_element = access_first_element(float_list)
    assert float_first_element == 3.14159
    print(f'First element of float_list: {float_first_element}')
    bool_first_element = access_first_element(boolean_list)
    assert bool_first_element == True
    print(f'First element of boolean_list: {bool_first_element}')