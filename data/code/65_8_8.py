def test_list_access():
    data = [10, 20, 30, 40, 50]
    try:
        index_to_check = 2
        actual_value = data[index_to_check]
        assert actual_value == 30
        print(f"Test passed for index {index_to_check}: Value is {actual_value}")
        index_out_of_bounds = 5
        try:
            data[index_out_of_bounds] = 999
        except IndexError as e:
            print(f"Test passed for index out of bounds: Caught expected error: {e}")
        else:
            assert False, "IndexError was not raised for out-of-bounds access"
        index_negative = -1
        try:
            value = data[index_negative]
            assert value == 50
            print(f"Test passed for negative index {index_negative}: Value is {value}")
        except IndexError as e:
            assert False, "IndexError was not raised for negative index access"
    except AssertionError as e:
        print(f"Test failed: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
if __name__ == '__main__':
    test_list_access()