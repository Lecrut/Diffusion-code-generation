def compare_adjacent_numbers(data):
    for i in range(len(data) - 1):
        if not isinstance(data[i], (int, float)) or not isinstance(data[i+1], (int, float)):
            raise TypeError("Adjacent elements must both be numerical.")
        num1 = data[i]
        num2 = data[i+1]
        if num1 != num2:
            return f"Mismatch found between {num1} and {num2}"
    return "All adjacent numbers are equal"
if __name__ == '__main__':
    test_data_1 = [1, 2, 3, 4]
    test_data_2 = [1, 2, 'a', 4]
    test_data_3 = [1.5, 2.5, 3.5]
    test_data_4 = [1, 2, 3, 'b']
    test_data_5 = [1, 2, 3]
    print(f"Test 1: {compare_adjacent_numbers(test_data_1)}")
    print(f"Test 2: {compare_adjacent_numbers(test_data_2)}")
    print(f"Test 3: {compare_adjacent_numbers(test_data_3)}")
    print(f"Test 4: {compare_adjacent_numbers(test_data_4)}")
    print(f"Test 5: {compare_adjacent_numbers(test_data_5)}")
    try:
        compare_adjacent_numbers(test_data_2)
    except TypeError as e:
        print(f"Caught expected error for Test 2: {e}")