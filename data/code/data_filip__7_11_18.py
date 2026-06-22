def has_no_special_characters(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    if not text:
        return True
    for char in text:
        if not char.isalnum():
            return False
    return True

if __name__ == '__main__':
    test_string = "HelloWorld123"
    result = has_no_special_characters(test_string)
    print(result)
    test_string_with_special = "Hello@World!"
    result_special = has_no_special_characters(test_string_with_special)
    print(result_special)