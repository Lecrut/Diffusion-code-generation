import re

class TextCleaner:
    def clean_and_split(self, text):
        cleaned_text = re.sub(r'[^\w\s]', '', text)
        return cleaned_text.split()

if __name__ == '__main__':
    cleaner = TextCleaner()
    sample_text = "This is a very long sentence, designed to test! the efficiency of word splitting; on extremely long strings? and ensure: that the time complexity & space usage are minimal, for large inputs."
    words = cleaner.clean_and_split(sample_text)
    print(words)