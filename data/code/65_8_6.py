def test_list_access():
    data = [10, 20, 30, 40, 50]
    try:
        index_to_access = 2
        actual_value = data[index_to_access]
        assert actual_value == 30
        print(f"Test 1 Passed: Element at index {index_to_access} is {actual_value}")
        index_out_of_bounds = 5
        try:
            data[index_out_of_bounds] = 999
        except IndexError:
            print("Test 2 Passed: Correctly caught IndexError for out-of-bounds access.")
        index_negative = -1
        actual_value_neg = data[index_negative]
        assert actual_value_neg == 50
        print(f"Test 3 Passed: Element at index {index_negative} (negative indexing) is {actual_value_neg}")
        index_out_of_bounds_negative = -6
        try:
            data[index_out_of_bounds_negative] = 1000
        except IndexError:
            print("Test 4 Passed: Correctly caught IndexError for out-of-bounds negative access.")
    except AssertionError as e:
        print(f"Assertion Failed: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
if __name__ == '__main__':
    test_list_access()