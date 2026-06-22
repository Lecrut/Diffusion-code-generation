class TextProcessor:
    @staticmethod
    def capitalize_word(word):
        return word.capitalize()
    
    def __init__(self, text):
        self.text = text
    
    def process_text(self):
        words = self.text.split()
        capitalized_words = [TextProcessor.capitalize_word(word) for word in words]
        return ' '.join(capitalized_words)

if __name__ == '__main__':
    sample_text = "innovating with artificial intelligence"
    processor = TextProcessor(sample_text)
    result = processor.process_text()
    print(result)