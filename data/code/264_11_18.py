import re

def extract_words(sentences):
    words = set()
    for sentence in sentences:
        words.update(re.findall(r'\b\w+\b', sentence.lower()))
    return sorted(words)

if __name__ == '__main__':
    sample_sentences = [
        "Hello world! This is a test sentence with numbers 123 and symbols @#.",
        "Multiple   spaces\tand\nnewlines are handled correctly. Word.",
        "Alpha beta gamma alpha"
    ]
    result = extract_words(sample_sentences)
    print(f"Distinct words sorted alphabetically: {result}")