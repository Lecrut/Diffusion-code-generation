def test_list_access(data, index, expected):
    assert index < 0, "Index must be non-negative"
    assert index < len(data), f"Index {index} is out of bounds for list of length {len(data)}"
    actual = data[index]
    assert actual == expected, f"Expected {expected} at index {index}, but got {actual}"
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    try:
        test_list_access(sample_list, 2, 30)
        print("Test 1 Passed: Correct element access.")
        test_list_access(sample_list, 0, 10)
        print("Test 2 Passed: First element access.")
        test_list_access(sample_list, 4, 50)
        print("Test 3 Passed: Last element access.")
        print("\nTesting Error Handling:")
        try:
            test_list_access(sample_list, 5, 99)
            print("Error Test Failed: Expected IndexError for out-of-bounds access.")
        except AssertionError as e:
            if "Index 5 is out of bounds" in str(e):
                print("Error Test Passed: Correctly caught index out of bounds error.")
            else:
                print(f"Error Test Failed: Caught wrong error type: {e}")
        except Exception as e:
            print(f"Error Test Caught unexpected exception: {e}")
        try:
            test_list_access(sample_list, -1, 10)
            print("Error Test Failed: Expected IndexError for negative index.")
        except AssertionError as e:
            if "Index must be non-negative" in str(e):
                print("Error Test Passed: Correctly caught negative index error.")
            else:
                print(f"Error Test Failed: Caught wrong error type: {e}")
        except Exception as e:
            print(f"Error Test Caught unexpected exception: {e}")
    except AssertionError as e:
        print(f"A primary test failed: {e}")