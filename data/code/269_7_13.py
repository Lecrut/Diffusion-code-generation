import string

PUNCTUATION_CHARS = set(string.punctuation)

def remove_duplicate_punctuation(text):
    seen = set()
    result = []
    for char in text:
        if char in PUNCTUATION_CHARS and char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)

if __name__ == '__main__':
    sample_string = "Hello, world! This is a test string with punctuation."
    result = remove_duplicate_punctuation(sample_string)
    print(result)