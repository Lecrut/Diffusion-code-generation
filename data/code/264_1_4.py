import re
def extract_words(text):
    words = set(re.findall(r'[a-zA-Z0-9]+', text))
    return words
if __name__ == '__main__':
    sample_string1 = "Hello world, this is a test string with numbers 123 and symbols! Python is fun."
    sample_string2 = "Word word word. Another one here: abc-def ghi."
    sample_string3 = "12345 and some punctuation... @#$"
    result1 = extract_words(sample_string1)
    print(f"Input: '{sample_string1}'")
    print(f"Output: {result1}")
    result2 = extract_words(sample_string2)
    print(f"Input: '{sample_string2}'")
    print(f"Output: {result2}")
    result3 = extract_words(sample_string3)
    print(f"Input: '{sample_string3}'")
    print(f"Output: {result3}")