def to_lower_string(input_string):
    return input_string.lower()
if __name__ == '__main__':
    sample1 = "HeLlO WoRlD"
    result1 = to_lower_string(sample1)
    print(f"Input: {sample1}, Output: {result1}")
    sample2 = "PYTHON"
    result2 = to_lower_string(sample2)
    print(f"Input: {sample2}, Output: {result2}")
    sample3 = "aBcDeFg"
    result3 = to_lower_string(sample3)
    print(f"Input: {sample3}, Output: {result3}")
    sample4 = ""
    result4 = to_lower_string(sample4)
    print(f"Input: '{sample4}', Output: '{result4}'")