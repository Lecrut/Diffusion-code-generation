def access_first_element(data):
    if not isinstance(data, list) or len(data) == 0:
        raise ValueError("Input must be a non-empty list")
    return data[0]

if __name__ == '__main__':
    int_list = [42, 84, 168]
    string_list = ["hello", "world", "python"]
    float_list = [3.14159, 2.71828, 1.41421]
    bool_list = [True, False, True]

    try:
        int_result = access_first_element(int_list)
        assert int_result == 42
        print(f"First element of int_list: {int_result}")
    except (ValueError, IndexError) as e:
        print(f"Error accessing first element of int_list: {e}")

    try:
        string_result = access_first_element(string_list)
        assert string_result == "hello"
        print(f"First element of string_list: {string_result}")
    except (ValueError, IndexError) as e:
        print(f"Error accessing first element of string_list: {e}")

    try:
        float_result = access_first_element(float_list)
        assert float_result == 3.14159
        print(f"First element of float_list: {float_result}")
    except (ValueError, IndexError) as e:
        print(f"Error accessing first element of float_list: {e}")

    try:
        bool_result = access_first_element(bool_list)
        assert bool_result == True
        print(f"First element of bool_list: {bool_result}")
    except (ValueError, IndexError) as e:
        print(f"Error accessing first element of bool_list: {e}")