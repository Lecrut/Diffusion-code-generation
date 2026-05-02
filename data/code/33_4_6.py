def filter_alphanumeric(input_string):
    result = ""
    for char in input_string:
        if char.isalnum():
            result += char
    return result
if __name__ == '__main__':
    test_string1 = "Hello World! 123"
    test_string2 = "This has spaces and symbols@#$"
    test_string3 = "OnlyLettersAndNumbers99"
    test_string4 = "!!!@#$%^&*() "
    print(filter_alphanumeric(test_string1))
    print(filter_alphanumeric(test_string2))
    print(filter_alphanumeric(test_string3))
    print(filter_alphanumeric(test_string4))