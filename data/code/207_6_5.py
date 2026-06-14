def find_largest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    largest = data[0]
    for item in data[1:]:
        if item > largest:
            largest = item
    return largest
if __name__ == '__main__':
    list1 = [3, 1, 4, 1, 5, 9, 2]
    expected1 = 9
    result1 = find_largest(list1)
    assert result1 == expected1, f"Test Case 1 Failed: Expected {expected1}, Got {result1}"
    print("Test Case 1 Passed")
    list2 = [-10, -5, -20, -1]
    expected2 = -1
    result2 = find_largest(list2)
    assert result2 == expected2, f"Test Case 2 Failed: Expected {expected2}, Got {result2}"
    print("Test Case 2 Passed")
    list3 = [-50, 10, -30, 0, 45]
    expected3 = 45
    result3 = find_largest(list3)
    assert result3 == expected3, f"Test Case 3 Failed: Expected {expected3}, Got {result3}"
    print("Test Case 3 Passed")
    list4 = [42]
    expected4 = 42
    result4 = find_largest(list4)
    assert result4 == expected4, f"Test Case 4 Failed: Expected {expected4}, Got {result4}"
    print("Test Case 4 Passed")
    list5 = []
    try:
        find_largest(list5)
        assert False, "Test Case 5 Failed: Expected ValueError for empty list, but function succeeded."
    except ValueError:
        print("Test Case 5 Passed (Caught expected ValueError)")
    except Exception as e:
        assert False, f"Test Case 5 Failed: Caught unexpected exception {e}"