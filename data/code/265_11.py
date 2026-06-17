import re
def extract_alphanumeric(input_string):
    return re.sub(r'[^a-zA-Z0-9]', '', input_string)
if __name__ == '__main__':
    test_string1 = "Hello World 123!"
    result1 = extract_alphanumeric(test_string1)
    print(f"Input: '{test_string1}', Output: '{result1}'")
    test_string2 = "Python3.10 is great."
    result2 = extract_alphanumeric(test_string2)
    print(f"Input: '{test_string2}', Output: '{result2}'")
    test_string3 = "$$$abc123xyz"
    result3 = extract_alphanumeric(test_string3)
    print(f"Input: '{test_string3}', Output: '{result3}'")
    test_string4 = "OnlyLetters"
    result4 = extract_alphanumeric(test_string4)
    print(f"Input: '{test_string4}', Output: '{result4}'")