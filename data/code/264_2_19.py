import re

def extract_distinct_words(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    words = re.findall(r'\b\w+\b', text.lower())
    distinct_words = sorted(set(words))
    return distinct_words

if __name__ == '__main__':
    sample_text = "Hello world hello Python programming is fun"
    print(extract_distinct_words(sample_text))