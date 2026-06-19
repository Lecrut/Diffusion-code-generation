class TextProcessor:
    DELIMITER = ' '

    @staticmethod
    def get_first_letters(text):
        words = text.split(TextProcessor.DELIMITER)
        return [word[0] for word in words if word]

if __name__ == '__main__':
    sample_string = "This is another unique example"
    result = TextProcessor.get_first_letters(sample_string)
    print(result)