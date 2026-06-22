class TextProcessor:
    SEPARATOR = ' '
    
    @staticmethod
    def capitalize_words(input_string):
        return TextProcessor.SEPARATOR.join(word.capitalize() for word in input_string.split(TextProcessor.SEPARATOR))
        
if __name__ == '__main__':
    sample_text = "this is a sample text"
    processor = TextProcessor()
    capitalized_text = processor.capitalize_words(sample_text)
    print(capitalized_text)