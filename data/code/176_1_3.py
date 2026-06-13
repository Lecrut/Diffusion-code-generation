import re
def extract_and_lowercase_words(text):
    words = re.findall(r'[a-zA-Z]+', text)
    lowercase_words = [word.lower() for word in words]
    return lowercase_words
if __name__ == '__main__':
    sample_string = "This is a sample string with numbers 123 and punctuation! Python programming is fun."
    result = extract_and_lowercase_words(sample_string)
    print(result)