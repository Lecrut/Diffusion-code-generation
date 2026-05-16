def find_odd_numbers(numbers):
    odd_numbers = []
    for num in numbers:
        if num % 2 != 0:
            odd_numbers.append(num)
    return odd_numbers
def test_find_odd_numbers():
    input1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    expected1 = [1, 3, 5, 7, 9]
    assert find_odd_numbers(input1) == expected1, f"Test Case 1 Failed: Input {input1}, Expected {expected1}, Got {find_odd_numbers(input1)}"
    input2 = [1, 3, 5, 7]
    expected2 = [1, 3, 5, 7]
    assert find_odd_numbers(input2) == expected2, f"Test Case 2 Failed: Input {input2}, Expected {expected2}, Got {find_odd_numbers(input2)}"
    input3 = [2, 4, 6, 8]
    expected3 = []
    assert find_odd_numbers(input3) == expected3, f"Test Case 3 Failed: Input {input3}, Expected {expected3}, Got {find_odd_numbers(input3)}"
    input4 = []
    expected4 = []
    assert find_odd_numbers(input4) == expected4, f"Test Case 4 Failed: Input {input4}, Expected {expected4}, Got {find_odd_numbers(input4)}"
    input5 = [-1, 0, 2, -3, 4]
    expected5 = [-1, -3]
    assert find_odd_numbers(input5) == expected5, f"Test Case 5 Failed: Input {input5}, Expected {expected5}, Got {find_odd_numbers(input5)}"
    print("All tests passed!")
if __name__ == '__main__':
    test_find_odd_numbers()