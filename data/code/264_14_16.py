import re

class TextProcessor:
    @staticmethod
    def extract_words(text):
        return re.findall(r'\b\w+\b', text)

    @staticmethod
    def filter_punctuation(words):
        punctuation = '.,!?;:'
        return [word.strip(punctuation) for word in words]

if __name__ == '__main__':
    processor = TextProcessor()
    sample_text = "Hello World! This is a Test String with numbers 123 and symbols @#$."
    extracted_words = processor.extract_words(sample_text)
    filtered_words = processor.filter_punctuation(extracted_words)
    print(filtered_words)