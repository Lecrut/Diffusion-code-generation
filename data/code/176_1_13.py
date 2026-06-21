import re

def extract_unique_words(text):
    WORD_PATTERN = r'\b\w+\b'
    words = re.findall(WORD_PATTERN, text)
    unique_words = []
    seen = set()
    for word in words:
        if word not in seen:
            unique_words.append(word)
            seen.add(word)
    return unique_words

if __name__ == '__main__':
    sample_string = "This is a Sample string with numbers 123 and punctuation! Python programming is fun."
    result = extract_unique_words(sample_string)
    print(result)