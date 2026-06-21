import re

def clean_and_split(phrase):
    return re.findall(r'\b\w+\b', phrase.lower())

if __name__ == '__main__':
    input_phrase = "This is a complex example phrase with various words and punctuation!"
    cleaned_words = clean_and_split(input_phrase)
    print(cleaned_words)