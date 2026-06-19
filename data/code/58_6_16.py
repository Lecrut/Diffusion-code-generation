def access_first_element(data):
    return data[0]

if __name__ == '__main__':
    SAMPLE_INT_LIST = [15, 25, 35]
    SAMPLE_STRING_LIST = ["dog", "cat", "mouse"]
    SAMPLE_FLOAT_LIST = [0.5, 1.5, 2.5]
    SAMPLE_BOOL_LIST = [False, True, False]

    int_result = access_first_element(SAMPLE_INT_LIST)
    assert int_result == 15
    print(f"First element of integer list: {int_result}")

    string_result = access_first_element(SAMPLE_STRING_LIST)
    assert string_result == "dog"
    print(f"First element of string list: {string_result}")

    float_result = access_first_element(SAMPLE_FLOAT_LIST)
    assert float_result == 0.5
    print(f"First element of float list: {float_result}")

    bool_result = access_first_element(SAMPLE_BOOL_LIST)
    assert bool_result == False
    print(f"First element of boolean list: {bool_result}")