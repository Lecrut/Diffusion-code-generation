class TextProcessor:
    SPACE_REMOVAL_TABLE = str.maketrans('', '', ' ')
    
    @staticmethod
    def remove_spaces(text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        return text.translate(TextProcessor.SPACE_REMOVAL_TABLE)

if __name__ == '__main__':
    sample_text1 = "This is a unique implementation with spaces."
    sample_text2 = 'Another example without any spaces.'
    sample_text3 = "Yet another variant with multiple spaces."
    
    processor = TextProcessor()
    print(processor.remove_spaces(sample_text1))
    print(processor.remove_spaces(sample_text2))
    print(processor.remove_spaces(sample_text3))