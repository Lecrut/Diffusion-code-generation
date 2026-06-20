import string

def has_special_chars(s):
    special_chars = set(string.punctuation + string.whitespace)
    original_len = len(s)
    stripped_len = len(''.join(c for c in s if c not in special_chars))
    return original_len != stripped_len

if __name__ == '__main__':
    test_string_1 = "HelloWorld"
    test_string_2 = "Hello@World"
    test_string_3 = "Normal Text!"
    test_string_4 = "NoSpecials123"
    
    print(has_special_chars(test_string_1))
    print(has_special_chars(test_string_2))
    print(has_special_chars(test_string_3))
    print(has_special_chars(test_string_4))