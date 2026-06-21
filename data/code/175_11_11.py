import re
SAMPLE_TEXT = 'this is a very long sentence designed to test the efficiency of word splitting on extremely long strings and ensure that the time complexity and space usage are minimal for large inputs.'

def clean_and_split_text(text):
    cleaned_text = re.sub('\\W+', ' ', text)
    words = cleaned_text.split()
    return words
if __name__ == '__main__':
    words = clean_and_split_text(SAMPLE_TEXT)
    print(words)