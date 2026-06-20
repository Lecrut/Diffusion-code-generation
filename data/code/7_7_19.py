import string

def contains_special_characters(s):
    special_chars = set(string.punctuation)
    stripped = ''.join(c for c in s if c not in special_chars)
    return len(s) != len(stripped)

if __name__ == '__main__':
    sample1 = "Hello, World!"
    sample2 = "HelloWorld"
    sample3 = "123#456$"
    print(contains_special_characters(sample1))
    print(contains_special_characters(sample2))
    print(contains_special_characters(sample3))