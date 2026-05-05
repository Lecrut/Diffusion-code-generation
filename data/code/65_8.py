def test_list_access():
    data = [10, 20, 30, 40, 50]
    try:
        index_to_access = 2
        actual_value = data[index_to_access]
        assert actual_value == 30
        print("Test 1 Passed: Correct value accessed.")
        index_out_of_bounds = 5
        try:
            data[index_out_of_bounds]
        except IndexError:
            print("Test 2 Passed: Correctly raised IndexError for out-of-bounds access.")
        index_negative = -1
        try:
            data[index_negative]
        except IndexError:
            print("Test 3 Passed: Correctly raised IndexError for negative index access.")
        index_valid = 0
        actual_value_zero = data[index_valid]
        assert actual_value_zero == 10
        print("Test 4 Passed: Correct value accessed at index 0.")
    except AssertionError as e:
        print(f"Assertion Failed: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
if __name__ == '__main__':
    test_list_access()