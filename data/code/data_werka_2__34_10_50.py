class TextProcessor:
    @staticmethod
    def capitalize_first_letter(word):
        return word[0].upper() + word[1:]
    
    def __init__(self, text):
        self.text = text
    
    def capitalize_words(self):
        words = self.text.split()
        capitalized_words = [TextProcessor.capitalize_first_letter(word) for word in words]
        return ' '.join(capitalized_words)

if __name__ == '__main__':
    sample_text = "innovating with artificial intelligence"
    processor = TextProcessor(sample_text)
    result = processor.capitalize_words()
    print(result)