def are_strings_equal(str1, str2):
    return str1 == str2
if __name__ == '__main__':
    print(are_strings_equal("hello", "hello"))
    print(are_strings_equal("hello", "world"))
    print(are_strings_equal("", ""))
    print(are_strings_equal("a", "b"))
    print(are_strings_equal("abc", "abc "))