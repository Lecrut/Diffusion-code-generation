def access_first_element(data):
    return data[0]
if __name__ == '__main__':
    int_list = [10, 20, 30]
    string_list = ["apple", "banana", "cherry"]
    result_int = access_first_element(int_list)
    assert result_int == 10
    print(f"First element of {int_list}: {result_int}")
    result_string = access_first_element(string_list)
    assert result_string == "apple"
    print(f"First element of {string_list}: {result_string}")
    float_list = [3.14, 2.71, 1.618]
    result_float = access_first_element(float_list)
    assert result_float == 3.14
    print(f"First element of {float_list}: {result_float}")
    bool_list = [True, False, True]
    result_bool = access_first_element(bool_list)
    assert result_bool == True
    print(f"First element of {bool_list}: {result_bool}")
    try:
        empty_list = []
        access_first_element(empty_list)
        assert False
    except IndexError:
        print("Successfully caught IndexError for an empty list.")