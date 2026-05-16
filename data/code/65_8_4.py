def test_list_access():
    data = [10, 20, 30, 40, 50]
    try:
        index_to_access = 2
        element = data[index_to_access]
        assert element == 30
        print("Test 1 Passed: Correct element accessed.")
        index_out_of_bounds = 5
        try:
            data[index_out_of_bounds]
            assert False, "Error: Index out of bounds was not raised."
        except IndexError:
            print("Test 2 Passed: IndexError correctly raised for out-of-bounds access.")
        index_negative = -1
        element_negative = data[index_negative]
        assert element_negative == 50
        print("Test 3 Passed: Negative indexing correctly accessed the last element.")
    except AssertionError as e:
        print(f"Test Failed: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
if __name__ == '__main__':
    test_list_access()