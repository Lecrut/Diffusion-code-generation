def case_insensitive_string_equality(str1, str2):
    return str1.lower() == str2.lower()
if __name__ == '__main__':
    print(case_insensitive_string_equality("Hello", "hello"))
    print(case_insensitive_string_equality("World", "world"))
    print(case_insensitive_string_equality("Python", "java"))
    print(case_insensitive_string_equality("Apple", "apple"))
    print(case_insensitive_string_equality("Test", "tEsT"))
    print(case_insensitive_string_equality("a", "A"))