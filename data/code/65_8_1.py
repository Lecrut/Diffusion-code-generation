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
        except IndexError:
            print("Test passed for IndexError: Correctly caught IndexError for index 5.")
        else:
            assert False, "IndexError was expected but not raised."
        index_negative = -1
        try:
            value = data[index_negative]
            assert value == 50
            print(f"Test passed for negative index {index_negative}: Value is {value}")
        except IndexError:
            assert False, "IndexError was expected for negative index -1."
        except Exception as e:
            assert False, f"Unexpected error for negative index: {e}"
    except AssertionError as e:
        print(f"Test failed: {e}")
    except Exception as e:
        print(f"An unexpected error occurred during testing: {e}")
if __name__ == '__main__':
    test_list_access()