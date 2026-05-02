def compare_strings_case_insensitive(str1, str2):
    return str1.lower() == str2.lower()
if __name__ == '__main__':
    print(compare_strings_case_insensitive("Hello", "hello"))
    print(compare_strings_case_insensitive("Python", "python"))
    print(compare_strings_case_insensitive("Apple", "Banana"))
    print(compare_strings_case_insensitive("Test", "test"))
    print(compare_strings_case_insensitive("aBc", "abc"))
    print(compare_strings_case_insensitive("same", "same"))