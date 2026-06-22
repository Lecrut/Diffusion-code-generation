import string

def has_special_characters(s):
    special_chars = set(string.punctuation)
    stripped = ''.join(c for c in s if c not in special_chars)
    return len(s) != len(stripped)

if __name__ == '__main__':
    sample_values = ["hello", "hello!", "world?123", "no_special", "has@symbol#"]
    for sample in sample_values:
        result = has_special_characters(sample)
        print(result)