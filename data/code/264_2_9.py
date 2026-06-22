import re

DISTINCT_WORDS_RE = re.compile(r'\b\w+\b')

def extract_distinct_words(text):
    words = DISTINCT_WORDS_RE.findall(text.lower())
    return sorted(set(words))

if __name__ == '__main__':
    sample_text = "Hello world hello Python programming is fun"
    print(extract_distinct_words(sample_text))