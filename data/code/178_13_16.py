import re

def extract_words(phrase):
    words = re.findall(r'\b\w+\b', phrase)
    return [word.lower() for word in words]

if __name__ == '__main__':
    sample_phrase = "This is a complex example phrase with various words and punctuation."
    result = extract_words(sample_phrase)
    print(result)