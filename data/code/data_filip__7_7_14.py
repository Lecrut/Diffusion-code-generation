import string

def has_special_characters(s: str) -> bool:
    stripped = ''.join(ch for ch in s if ch not in string.punctuation and not ch.isspace())
    return len(s) != len(stripped)

if __name__ == '__main__':
    sample_strings = ["hello_world", "hello world!", "no_special"]
    for s in sample_strings:
        result = has_special_characters(s)
        print(result)