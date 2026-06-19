def access_first_element(data):
    return data[0]
if __name__ == '__main__':
    int_list = [5, 15, 25]
    int_result = access_first_element(int_list)
    assert int_result == 5
    print(f'Integer list first element: {int_result}')
    string_list = ['hello', 'world', 'python']
    string_result = access_first_element(string_list)
    assert string_result == 'hello'
    print(f'String list first element: {string_result}')
    float_list = [0.1, 0.2, 0.3]
    float_result = access_first_element(float_list)
    assert float_result == 0.1
    print(f'Float list first element: {float_result}')
    bool_list = [False, True, False]
    bool_result = access_first_element(bool_list)
    assert bool_result == False
    print(f'Boolean list first element: {bool_result}')