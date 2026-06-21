import re

def clean_phrase(phrase):
    return re.sub(r'[^a-zA-Z0-9\s]', '', phrase)

def extract_words(phrase):
    cleaned_phrase = clean_phrase(phrase)
    words = re.findall(r'\b\w+\b', cleaned_phrase.lower())
    return words

if __name__ == '__main__':
    sample_phrase = "This is a complex example phrase with various words and punctuation!"
    result = extract_words(sample_phrase)
    print(result)