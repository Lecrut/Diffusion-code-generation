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
        try:
            value = data[index_negative]
            assert value == 50
            print(f"Test 3 Passed: Negative indexing access at {index_negative} is {value}")
        except Exception as e:
            print(f"Test 3 Failed: Unexpected error for negative indexing: {e}")
    except AssertionError as e:
        print(f"Test Failed: Assertion Error: {e}")
    except Exception as e:
        print(f"Test Failed: Unexpected Error: {e}")
if __name__ == '__main__':
    test_list_access()