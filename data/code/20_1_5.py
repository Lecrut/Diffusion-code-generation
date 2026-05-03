def are_strings_equal_insensitive(str1, str2):
    return str1.lower() == str2.lower()
if __name__ == '__main__':
    print(are_strings_equal_insensitive("Hello", "hello"))
    print(are_strings_equal_insensitive("Python", "python"))
    print(are_strings_equal_insensitive("World", "earth"))
    print(are_strings_equal_insensitive("Apple", "Banana"))
    print(are_strings_equal_insensitive("Test", "test"))