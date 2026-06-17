import re
def extract_words(text):
    words = re.findall(r'[a-zA-Z0-9]+', text)
    return set(words)
if __name__ == '__main__':
    sample_text1 = "Hello world, this is a test. Python programming is fun 123."
    sample_text2 = "  Multiple   spaces \t and newlines \n are handled correctly. Word word."
    sample_text3 = "Alpha beta gamma delta 12345"
    result1 = extract_words(sample_text1)
    print(f"Result for sample_text1: {result1}")
    result2 = extract_words(sample_text2)
    print(f"Result for sample_text2: {result2}")
    result3 = extract_words(sample_text3)
    print(f"Result for sample_text3: {result3}")