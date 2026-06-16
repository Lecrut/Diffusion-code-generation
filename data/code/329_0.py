def are_strings_equal(str1, str2):
    return str1 == str2
if __name__ == '__main__':
    print(are_strings_equal("hello", "hello"))
    print(are_strings_equal("world", "hello"))
    print(are_strings_equal("", ""))
    print(are_strings_equal("abc", "abcd"))
    print(are_strings_equal("Python", "python"))