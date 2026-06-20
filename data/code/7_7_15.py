import string

def has_special_characters(s):
    special_chars = set(string.punctuation + string.whitespace)
    stripped = ''.join(c for c in s if c not in special_chars)
    return len(stripped) < len(s)

if __name__ == '__main__':
    samples = [
        "hello world",
        "hello@world!",
        "normal123",
        "100%",
        "no special",
        "has#special"
    ]
    for sample in samples:
        print(has_special_characters(sample))