import re
def find_all_words(text):
    return re.findall(r'\b\w+\b', text)
if __name__ == '__main__':
    sample_string = "This is a sample string with various words and some punctuation! 123."
    words = find_all_words(sample_string)
    print(words)