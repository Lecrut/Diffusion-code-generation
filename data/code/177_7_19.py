class StringProcessor:
    DELIMITER = ' '

    @staticmethod
    def split_string(input_string):
        return input_string.split(StringProcessor.DELIMITER)

if __name__ == '__main__':
    sample_text = 'Python is awesome'
    processed_words = StringProcessor.split_string(sample_text)
    print(processed_words)