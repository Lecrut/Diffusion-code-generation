import re
def extract_alphanumeric(input_string):
    return "".join(char for char in input_string if char.isalnum())
if __name__ == '__main__':
    test_string1 = "Hello World 123!"
    result1 = extract_alphanumeric(test_string1)
    print(f"Input: '{test_string1}'")
    print(f"Output: '{result1}'")
    test_string2 = "Python3.10 is great."
    result2 = extract_alphanumeric(test_string2)
    print(f"Input: '{test_string2}'")
    print(f"Output: '{result2}'")
    test_string3 = "$$%^&*()_+=-"
    result3 = extract_alphanumeric(test_string3)
    print(f"Input: '{test_string3}'")
    print(f"Output: '{result3}'")