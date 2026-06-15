import re
def fast_word_splitter(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return words
if __name__ == '__main__':
    sample_text = "This is a large block of text designed to test the efficiency of word separation algorithms. Words are separated by spaces and punctuation marks like commas and periods."
    print(fast_word_splitter(sample_text))