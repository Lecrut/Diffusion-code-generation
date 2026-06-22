def remove_spaces(input_string):
    if not isinstance(input_string, str):
        raise ValueError('Input must be a string')
    return ''.join(input_string.split())
if __name__ == '__main__':
    test_string1 = 'hello world'
    result1 = remove_spaces(test_string1)
    print(result1)
    test_string2 = '   this has spaces   '
    result2 = remove_spaces(test_string2)
    print(result2)
    test_string3 = 'no_spaces'
    result3 = remove_spaces(test_string3)
    print(result3)