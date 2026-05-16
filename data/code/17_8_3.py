def is_even(number):
    return number % 2 == 0
if __name__ == '__main__':
    test_cases = [
        (0, True),
        (1, False),
        (2, True),
        (-4, True),
        (-5, False),
        (100, True),
        (-1, False),
        (-2, True)
    ]
    for number, expected in test_cases:
        result = is_even(number)
        assert result == expected, f"Input: {number}, Expected: {expected}, Got: {result}"
        print(f"Test passed for {number}: is_even({number}) == {expected}")
    print("All test cases passed!")