import re
def extract_words(phrase):
    return re.findall(r'\b\w+\b', phrase)
if __name__ == '__main__':
    input_phrase = "This is a complex example phrase with various punctuation marks and numbers 123."
    words = extract_words(input_phrase)
    print(words)