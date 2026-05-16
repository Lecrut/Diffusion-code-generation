def access_first_element(data):
    return data[0]
if __name__ == '__main__':
    int_list = [10, 20, 30]
    string_list = ["apple", "banana", "cherry"]
    float_list = [1.5, 2.5, 3.5]
    int_result = access_first_element(int_list)
    string_result = access_first_element(string_list)
    float_result = access_first_element(float_list)
    assert int_result == 10
    assert string_result == "apple"
    assert float_result == 1.5
    print("All assertions passed.")