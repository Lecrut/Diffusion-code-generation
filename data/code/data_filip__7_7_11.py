import string

def has_special_characters(s):
    special_chars = set(string.punctuation)
    original_length = len(s)
    stripped_length = len("".join(c for c in s if c not in special_chars))
    return original_length != stripped_length

if __name__ == '__main__':
    sample_string_1 = "HelloWorld"
    sample_string_2 = "Hello@World"
    sample_string_3 = "Test#123"
    print(has_special_characters(sample_string_1))
    print(has_special_characters(sample_string_2))
    print(has_special_characters(sample_string_3))