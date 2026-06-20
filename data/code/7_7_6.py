import string

def has_special_chars(s):
    special_chars = set(string.punctuation)
    stripped = ''.join(c for c in s if c not in special_chars)
    return len(s) != len(stripped)

if __name__ == '__main__':
    samples = ["hello", "hello!", "world@123", "no special", "has#hash"]
    for sample in samples:
        print(has_special_chars(sample))