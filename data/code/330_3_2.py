def to_uppercase(s):
    result = ""
    for char in s:
        result += chr(ord(char) - 32)
    return result
if __name__ == '__main__':
    test_string = "hello world"
    uppercase_string = to_uppercase(test_string)
    print(uppercase_string)