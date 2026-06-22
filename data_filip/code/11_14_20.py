from collections import Counter

def get_duplicate_chars(text):
    freq = Counter(text)
    return {char: count for char, count in freq.items() if count > 1}

if __name__ == '__main__':
    sample_text = "Hello, World! This is a test string with repeated characters: H e l l o."
    result = get_duplicate_chars(sample_text)
    print(result)