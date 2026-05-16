def filter_alphanumeric(input_string):
    result = ""
    for char in input_string:
        if char.isalnum():
            result += char
    return result
if __name__ == '__main__':
    sample1 = "Hello World! 123"
    sample2 = "This is a test string with symbols @#$."
    sample3 = "OnlyLettersAndNumbers456"
    sample4 = "Spaces and symbols  with    extra   stuff"
    print(filter_alphanumeric(sample1))
    print(filter_alphanumeric(sample2))
    print(filter_alphanumeric(sample3))
    print(filter_alphanumeric(sample4))