def extract_alphanumeric(input_string):
    result = ""
    for char in input_string:
        if char.isalnum():
            result += char
    return result
if __name__ == '__main__':
    test_string1 = "Hello World 123!"
    test_string2 = "Python3.10 is great"
    test_string3 = "$$%^&*() "
    test_string4 = ""
    print(f"'{test_string1}' -> '{extract_alphanumeric(test_string1)}'")
    print(f"'{test_string2}' -> '{extract_alphanumeric(test_string2)}'")
    print(f"'{test_string3}' -> '{extract_alphanumeric(test_string3)}'")
    print(f"'{test_string4}' -> '{extract_alphanumeric(test_string4)}'")