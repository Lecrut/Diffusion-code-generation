def test_list_access():
    data = [10, 20, 30, 40, 50]
    try:
        index_to_access = 2
        actual_value = data[index_to_access]
        assert actual_value == 30
        print(f"Test passed for index {index_to_access}: Value is {actual_value}")
        index_out_of_bounds = 5
        try:
            data[index_out_of_bounds] = 999
        except IndexError as e:
            print(f"Test passed for index out of bounds: Caught expected error: {e}")
        index_negative = -1
        try:
            data[index_negative] = 1000
        except IndexError as e:
            print(f"Test passed for negative index: Caught expected error: {e}")
    except AssertionError as e:
        print(f"Test failed: Assertion error occurred: {e}")
    except Exception as e:
        print(f"Test failed: An unexpected error occurred: {e}")
if __name__ == '__main__':
    test_list_access()