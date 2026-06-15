import re
def find_words(text):
    return re.findall(r'\b\w+\b', text)
if __name__ == '__main__':
    sample_string = "This is a sample string with various words and some punctuation! How are you doing today?"
    words = find_words(sample_string)
    print(words)