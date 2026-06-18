def are_equal(a: object, b: object) -> bool:
    return a == b
if __name__ == '__main__':
    int_val = 42
    str_val = "hello"
    list_val = [1, 2, 3]
    dict_val = {'key': 'value'}
    print(are_equal(int_val, int_val))                       
    print(are_equal(str_val, str_val))                        
    print(are_equal(list_val, list_val))                                                                                                                             
    print(are_equal(dict_val, dict_val))                                                                 
    assert are_equal(int_val, int_val), "Integers should be equal"
    assert not are_equal(list_val, [4, 5]), "Lists with different content should not be equal"