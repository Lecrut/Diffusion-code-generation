import re

def extract_and_sort_words(sentences):
    words = set()
    for sentence in sentences:
        words.update(re.findall(r'\b\w+\b', sentence))
    return sorted(words)

if __name__ == '__main__':
    sample_texts = [
        "Hello world! This is a test sentence with numbers 123 and symbols @#.",
        "Multiple   spaces\tand\nnewlines are handled correctly. Word test again.",
        "Alpha beta Gamma delta 12345"
    ]
    result = extract_and_sort_words(sample_texts)
    print(f"Distinct sorted words: {result}")