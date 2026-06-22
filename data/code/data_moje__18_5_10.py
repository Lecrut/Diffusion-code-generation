def find_middle_index_and_value(arr):
    if not arr:
        return None, None
    mid_index = len(arr) // 2
    mid_value = arr[mid_index]
    return mid_index, mid_value

if __name__ == '__main__':
    test_cases = [
        ([1, 2, 3, 4, 5], (2, 3)),
        ([10, 20], (1, 20)),
        ([7], (0, 7)),
        ([1, 2, 3, 4], (2, 3)),
        ([-5, -2, 0, 3, 9], (2, 0))
    ]
    
    all_passed = True
    for i, (input_arr, expected) in enumerate(test_cases):
        result = find_middle_index_and_value(input_arr)
        if result != expected:
            all_passed = False
            print(f"Test case {i + 1} failed: expected {expected}, got {result}")
        else:
            print(f"Test case {i + 1} passed: {result}")
            
    if all_passed:
        print("All tests passed.")