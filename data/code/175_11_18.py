import re

class TextCleaner:
    def clean_and_split(self, text):
        cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
        return cleaned_text.split()

if __name__ == '__main__':
    cleaner = TextCleaner()
    long_text = "this is a very long sentence! designed to test the efficiency of word splitting on extremely long strings? for time and space optimization."
    words = cleaner.clean_and_split(long_text)
    print(words)