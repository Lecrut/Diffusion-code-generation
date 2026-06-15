import re
def extract_words(text):
    words = re.findall(r'[a-zA-Z0-9]+', text)
    return set(words)
if __name__ == '__main__':
    sample_text1 = "Hello world! This is a test sentence with 123 numbers."
    result1 = extract_words(sample_text1)
    print(f"Sample 1: {result1}")
    sample_text2 = "  Multiple   spaces\tand\nnewlines\there. End."
    result2 = extract_words(sample_text2)
    print(f"Sample 2: {result2}")
    sample_text3 = "AlphaNumeric123 BetaGamma"
    result3 = extract_words(sample_text3)
    print(f"Sample 3: {result3}")