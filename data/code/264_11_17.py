import re

def validate_input(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")

def extract_words(text):
    validate_input(text)
    words = re.findall(r'\b\w+\b', text.lower())
    return sorted(set(words))

if __name__ == '__main__':
    sample_text1 = "Hello world! This is a test sentence with numbers 123 and symbols @#."
    sample_text2 = "  Multiple   spaces\tand\nnewlines are handled correctly. Word."
    sample_text3 = "Alpha beta gamma alpha"
    result1 = extract_words(sample_text1)
    print(f"Result 1: {result1}")
    result2 = extract_words(sample_text2)
    print(f"Result 2: {result2}")
    result3 = extract_words(sample_text3)
    print(f"Result 3: {result3}")