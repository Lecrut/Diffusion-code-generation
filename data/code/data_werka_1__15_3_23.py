def compare_strings(str1, str2):
    return str1.lower() == str2.lower()

if __name__ == '__main__':
    str1 = "Hello"
    str2 = "hello"
    result = compare_strings(str1, str2)
    print(result)