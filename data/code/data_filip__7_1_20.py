def contains_special_chars(s):
    for char in s:
        code = ord(char)
        if code < 32 or code == 127:
            return True
        if 33 <= code <= 47 or 58 <= code <= 64 or 91 <= code <= 96 or 123 <= code <= 126:
            return True
    return False

if __name__ == '__main__':
    sample_string_1 = "Hello World!"
    sample_string_2 = "HelloWorld"
    sample_string_3 = "Test@123#"
    
    print(contains_special_chars(sample_string_1))
    print(contains_special_chars(sample_string_2))
    print(contains_special_chars(sample_string_3))