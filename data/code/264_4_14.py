import re

def find_distinct_words(text):
    words = set()
    for word in re.findall(r'\b\w+\b', text.lower()):
        words.add(word)
    return words

if __name__ == '__main__':
    sample_string = "This is a test string with repeated words and some punctuation."
    result = find_distinct_words(sample_string)
    print(result)