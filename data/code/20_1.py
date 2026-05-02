import operator
def case_insensitive_string_equality(s1, s2):
    return s1.lower() == s2.lower()
if __name__ == '__main__':
    str1 = "Hello"
    str2 = "hello"
    str3 = "World"
    str4 = "world"
    str5 = "Python"
    str6 = "java"
    print(f"'{str1}' and '{str2}': {case_insensitive_string_equality(str1, str2)}")
    print(f"'{str3}' and '{str4}': {case_insensitive_string_equality(str3, str4)}")
    print(f"'{str5}' and '{str6}': {case_insensitive_string_equality(str5, str6)}")
    print(f"'{str1}' and '{str3}': {case_insensitive_string_equality(str1, str3)}")
    print(f"'{str1}' and '{str5}': {case_insensitive_string_equality(str1, str5)}")