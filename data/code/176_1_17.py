import re

def extract_unique_words(text):
    words = re.findall(r'\b\w+\b', text)
    unique_words = []
    seen = set()
    
    for word in words:
        lower_word = word.lower()
        if lower_word not in seen:
            seen.add(lower_word)
            unique_words.append(word)
    
    return unique_words

if __name__ == '__main__':
    sample_string = "Hello World! This is a test string with numbers 123 and punctuation."
    result = extract_unique_words(sample_string)
    print(result)