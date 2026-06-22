def compare_strings(str1, str2):
    return str1.lower() == str2.lower()

if __name__ == '__main__':
    STRING_ONE = "Hello"
    STRING_TWO = "hello"
    result = compare_strings(STRING_ONE, STRING_TWO)
    print(result)