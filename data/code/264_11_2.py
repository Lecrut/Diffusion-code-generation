import re
def extract_words(text):
    words = re.findall(r'[a-zA-Z0-9]+', text)
    return set(words)
if __name__ == '__main__':
    sample_text1 = "Hello world! This is a test sentence with numbers 123 and symbols @#."
    sample_text2 = "  Multiple   spaces\tand\nnewlines are handled well. Word test again."
    sample_text3 = "Alpha beta gamma delta 12345"
    result1 = extract_words(sample_text1)
    print(f"Sample 1: {result1}")
    result2 = extract_words(sample_text2)
    print(f"Sample 2: {result2}")
    result3 = extract_words(sample_text3)
    print(f"Sample 3: {result3}")