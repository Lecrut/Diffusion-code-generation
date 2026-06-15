import re
def find_all_words(text):
    words = set()
    for word in re.findall(r'\b\w+\b', text.lower()):
        words.add(word)
    return list(words)
if __name__ == '__main__':
    sample_string_1 = "Hello world! This is a test, and world again."
    sample_string_2 = "Python programming is fun. Is it easy? Yes, it is."
    sample_string_3 = "  Multiple   spaces and Punctuation!  "
    result_1 = find_all_words(sample_string_1)
    print(f"Input: '{sample_string_1}'")
    print(f"Output: {result_1}")
    result_2 = find_all_words(sample_string_2)
    print(f"Input: '{sample_string_2}'")
    print(f"Output: {result_2}")
    result_3 = find_all_words(sample_string_3)
    print(f"Input: '{sample_string_3}'")
    print(f"Output: {result_3}")