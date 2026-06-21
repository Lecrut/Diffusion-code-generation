import re

def extract_words(phrase):
    if not isinstance(phrase, str):
        raise ValueError("Input must be a string.")
    
    return re.findall(r'\b\w+\b', phrase)

if __name__ == '__main__':
    sample_phrase = "This is a complex example phrase with various words and punctuation."
    words = extract_words(sample_phrase)
    print(words)