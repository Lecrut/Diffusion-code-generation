def are_strings_equal(str1, str2):
    return str1.lower() == str2.lower()
if __name__ == '__main__':
    print(are_strings_equal("Hello", "hello"))
    print(are_strings_equal("World", "world"))
    print(are_strings_equal("Python", "Java"))
    print(are_strings_equal("Test", "test"))
    print(are_strings_equal("aBc", "abc"))