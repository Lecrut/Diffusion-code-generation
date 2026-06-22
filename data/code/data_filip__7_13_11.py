def has_special_char(s):
    for char in s:
        if not char.isalnum() and char != ' ':
            return True
    return False

if __name__ == '__main__':
    test_string = "Hello World! Python 3.9"
    result = has_special_char(test_string)
    print(result)