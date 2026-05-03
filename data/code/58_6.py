def access_first_element(data):
    return data[0]
if __name__ == '__main__':
    int_list = [10, 20, 30]
    string_list = ["apple", "banana", "cherry"]
    int_result = access_first_element(int_list)
    assert int_result == 10
    print(f"Integer list first element: {int_result}")
    string_result = access_first_element(string_list)
    assert string_result == "apple"
    print(f"String list first element: {string_result}")
    float_list = [3.14, 2.71, 1.618]
    float_result = access_first_element(float_list)
    assert float_result == 3.14
    print(f"Float list first element: {float_result}")
    bool_list = [True, False, True]
    bool_result = access_first_element(bool_list)
    assert bool_result == True
    print(f"Boolean list first element: {bool_result}")
    try:
        empty_list = []
        access_first_element(empty_list)
        assert False
    except IndexError:
        print("Successfully caught IndexError for empty list.")
        pass