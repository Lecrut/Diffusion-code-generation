import re
def extract_alphanumeric(input_string):
    return "".join(char for char in input_string if char.isalnum())
if __name__ == '__main__':
    test_string1 = "Hello World 123!"
    result1 = extract_alphanumeric(test_string1)
    print(f"Input: '{test_string1}', Output: '{result1}'")
    test_string2 = "Python3.10 is fast"
    result2 = extract_alphanumeric(test_string2)
    print(f"Input: '{test_string2}', Output: '{result2}'")
    test_string3 = "OnlySymbols!@#$"
    result3 = extract_alphanumeric(test_string3)
    print(f"Input: '{test_string3}', Output: '{result3}'")
    test_string4 = ""
    result4 = extract_alphanumeric(test_string4)
    print(f"Input: '{test_string4}', Output: '{result4}'")