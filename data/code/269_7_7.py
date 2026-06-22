def remove_duplicate_punctuation(text):
    seen = set()
    result = []
    for char in text:
        if char.isalpha() or char.isdigit():
            seen.clear()
        elif char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)

if __name__ == '__main__':
    sample_text = "Hello, world! This is a test. Hello, Python!"
    print(remove_duplicate_punctuation(sample_text))