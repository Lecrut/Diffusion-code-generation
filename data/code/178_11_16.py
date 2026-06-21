import re

def extract_alphanumeric_words(phrase):
    words = re.findall(r'\b\w+\b', phrase)
    return [word for word in words if word.isalnum()]

if __name__ == '__main__':
    test_phrase1 = "Hello, world! This is a test phrase with 123 numbers."
    result1 = extract_alphanumeric_words(test_phrase1)
    print(f"Phrase: '{test_phrase1}'")
    print(f"Extracted words: {result1}")

    test_phrase2 = "Python programming is fun and easy (42)."
    result2 = extract_alphanumeric_words(test_phrase2)
    print(f"Phrase: '{test_phrase2}'")
    print(f"Extracted words: {result2}")

    test_phrase3 = "NoWordsHere!@# 12345."
    result3 = extract_alphanumeric_words(test_phrase3)
    print(f"Phrase: '{test_phrase3}'")
    print(f"Extracted words: {result3}")