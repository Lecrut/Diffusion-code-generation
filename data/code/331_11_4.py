def to_lower_string(input_string):
    return input_string.lower()
if __name__ == '__main__':
    test_string1 = "HeLlO WoRlD"
    result1 = to_lower_string(test_string1)
    print(f"Input: {test_string1}, Output: {result1}")
    test_string2 = "PYTHON"
    result2 = to_lower_string(test_string2)
    print(f"Input: {test_string2}, Output: {result2}")
    test_string3 = "aBcDeFg"
    result3 = to_lower_string(test_string3)
    print(f"Input: {test_string3}, Output: {result3}")
    test_string4 = ""
    result4 = to_lower_string(test_string4)
    print(f"Input: '{test_string4}', Output: '{result4}'")