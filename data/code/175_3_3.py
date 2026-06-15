import re
def separate_words(text):
    words = re.findall(r'\b\w+\b', text)
    return words
if __name__ == '__main__':
    sample_string1 = "Hello world! This is a test, with various spaces and punctuation."
    sample_string2 = "  \tWord1, Word2; Word3... "
    sample_string3 = "NoPunctuationHere"
    result1 = separate_words(sample_string1)
    result2 = separate_words(sample_string2)
    result3 = separate_words(sample_string3)
    print(f"Input: '{sample_string1}'")
    print(f"Output: {result1}")
    print("-" * 20)
    print(f"Input: '{sample_string2}'")
    print(f"Output: {result2}")
    print("-" * 20)
    print(f"Input: '{sample_string3}'")
    print(f"Output: {result3}")