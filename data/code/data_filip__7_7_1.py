import string

def contains_special_characters(s):
    stripped = ''.join(c for c in s if c not in string.punctuation)
    return len(s) != len(stripped)

if __name__ == '__main__':
    samples = ["hello", "hello!", "world?#", "abc123", "test@#"]
    for sample in samples:
        result = contains_special_characters(sample)
        print(result)