def check_string_equality(str1, str2):
    return str1 == str2
if __name__ == '__main__':
    s1 = "a" * 1000000
    s2 = "a" * 1000000
    s3 = "a" * 1000000 + "b"
    s4 = s1
    print(f"s1 == s2: {check_string_equality(s1, s2)}")
    print(f"s1 == s3: {check_string_equality(s1, s3)}")
    print(f"s1 == s4: {check_string_equality(s1, s4)}")