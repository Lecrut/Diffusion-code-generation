def filter_alphanumeric(input_string):
    result = ""
    for char in input_string:
        if char.isalnum():
            result += char
    return result
if __name__ == '__main__':
    sample1 = "Hello World! 123"
    sample2 = "This has spaces and symbols@#$"
    sample3 = "OnlyLettersAndNumbers987"
    sample4 = "!!!@#$%^&*() "
    print(f"Input: '{sample1}' -> Output: '{filter_alphanumeric(sample1)}'")
    print(f"Input: '{sample2}' -> Output: '{filter_alphanumeric(sample2)}'")
    print(f"Input: '{sample3}' -> Output: '{filter_alphanumeric(sample3)}'")
    print(f"Input: '{sample4}' -> Output: '{filter_alphanumeric(sample4)}'")