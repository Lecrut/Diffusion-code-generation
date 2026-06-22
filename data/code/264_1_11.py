import re
from collections import Counter

def count_word_frequencies(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return dict(Counter(words))

if __name__ == '__main__':
    sample_string1 = "Hello world! This is a test string with numbers 123 and symbols @#."
    sample_result1 = count_word_frequencies(sample_string1)
    print(f"Input: '{sample_string1}'")
    print(f"Output: {sample_result1}")

    sample_string2 = "Python programming is fun, isn't it? Python is great."
    sample_result2 = count_word_frequencies(sample_string2)
    print(f"Input: '{sample_string2}'")
    print(f"Output: {sample_result2}")