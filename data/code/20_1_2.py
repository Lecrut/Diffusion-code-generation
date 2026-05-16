def case_insensitive_string_equality(str1, str2):
    return str1.lower() == str2.lower()
if __name__ == '__main__':
    print(case_insensitive_string_equality("Hello", "hello"))
    print(case_insensitive_string_equality("Python", "python"))
    print(case_insensitive_string_equality("Apple", "Orange"))
    print(case_insensitive_string_equality("Test", "test"))
    print(case_insensitive_string_equality("aBc", "abc"))