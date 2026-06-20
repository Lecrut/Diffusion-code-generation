import string

def count_special_characters(s):
    special_chars = set(string.punctuation)
    count = sum(1 for char in s if char in special_chars)
    return count, count > 0

if __name__ == '__main__':
    sample_strings = [
        "Hello, World!",
        "NoSpecialCharsHere",
        "Special!@#$%^&*()",
        "Mixed 123 and symbols !@#"
    ]
    for sample in sample_strings:
        count, has_special = count_special_characters(sample)
        print((sample, count, has_special))