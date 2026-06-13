import re
class TextProcessor:
    def get_words(self, text):
        return re.findall(r'\b\w+\b', text)
if __name__ == '__main__':
    processor = TextProcessor()
    sample_text = "This is a sample sentence for testing word extraction."
    words = processor.get_words(sample_text)
    print(words)