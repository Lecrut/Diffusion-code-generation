def has_special_characters(s):
    special_chars = "!@#$%^&*()_+-=[]{}|;:',.<>?/\\`~"
    return any(char in special_chars for char in s)

if __name__ == '__main__':
    sample_string_1 = "HelloWorld"
    sample_string_2 = "Hello@World"
    print(has_special_characters(sample_string_1))
    print(has_special_characters(sample_string_2))