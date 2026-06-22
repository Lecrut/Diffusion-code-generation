def remove_spaces(input_string):
    return ''.join(input_string.split())

if __name__ == '__main__':
    test_string1 = "hello world"
    print(remove_spaces(test_string1))
    test_string2 = "   this has spaces   "
    print(remove_spaces(test_string2))
    test_string3 = "no_spaces"
    print(remove_spaces(test_string3))