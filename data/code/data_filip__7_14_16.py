SPECIAL_CHARACTERS = set("!@#$%^&*()_+-=[]{}|;':\",./<>?~`")

def has_special_characters(s):
    return bool(set(s) & SPECIAL_CHARACTERS)

if __name__ == '__main__':
    sample_strings = ["hello", "hello!", "world123", "test@value"]
    for sample in sample_strings:
        print(has_special_characters(sample))