def extract_alphanumeric(input_string):
    result = []
    for char in input_string:
        if char.isalnum():
            result.append(char)
    return "".join(result)
if __name__ == '__main__':
    test_string1 = "Hello World 123!"
    print(extract_alphanumeric(test_string1))
    test_string2 = "abc123xyz"
    print(extract_alphanumeric(test_string2))
    test_string3 = "NoAlphanumericChars"
    print(extract_alphanumeric(test_string3))
    test_string4 = ""
    print(extract_alphanumeric(test_string4))