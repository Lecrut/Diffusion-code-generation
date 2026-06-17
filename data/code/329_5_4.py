def check_string_equality(str1, str2):
    return str1 == str2
if __name__ == '__main__':
    s1 = "a" * 1000000
    s2 = "a" * 1000000
    s3 = "b" * 1000000
    print(check_string_equality(s1, s2))
    print(check_string_equality(s1, s3))