def are_strings_equal(str1, str2):
    return str1.lower() == str2.lower()

if __name__ == '__main__':
    string1 = "Hello"
    string2 = "hello"
    result = are_strings_equal(string1, string2)
    print(result)