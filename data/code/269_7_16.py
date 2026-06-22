import string

def remove_duplicate_punctuation(text):
    seen_punctuation = set()
    result = []
    for char in text:
        if char in string.punctuation and char not in seen_punctuation:
            seen_punctuation.add(char)
            result.append(char)
    return ''.join(result)

if __name__ == '__main__':
    sample_string = "Hello, world! This is a test string with punctuation. (And some more?)"
    cleaned_string = remove_duplicate_punctuation(sample_string)
    print(cleaned_string)