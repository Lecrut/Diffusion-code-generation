import re
def find_words(text):
    return re.findall(r'\b\w+\b', text)
if __name__ == '__main__':
    sample_string = "This is a sample string with various words and punctuation! How about this?"
    words = find_words(sample_string)
    print(words)