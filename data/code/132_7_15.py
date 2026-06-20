def is_valid_input(s):
    if not s:
        return False
    if not s.isalpha():
        return False
    return True

if __name__ == '__main__':
    test_strings = ["HelloWorld", "", "123", "Python3"]
    for string in test_strings:
        print(f"'{string}': {is_valid_input(string)}")