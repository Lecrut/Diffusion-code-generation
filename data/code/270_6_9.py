def remove_spaces(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    
    result = ''
    for char in input_string:
        if char != ' ':
            result += char
    return result

if __name__ == '__main__':
    test_string1 = "hello world"
    print(remove_spaces(test_string1))
    test_string2 = "   this has spaces   "
    print(remove_spaces(test_string2))
    test_string3 = "no_spaces"
    print(remove_spaces(test_string3))