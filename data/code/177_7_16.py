class StringProcessor:
    SEPARATOR = ' '

    @staticmethod
    def split_string(input_string):
        return input_string.split(StringProcessor.SEPARATOR)

if __name__ == '__main__':
    sample_text = 'Python is awesome'
    processor = StringProcessor()
    words = processor.split_string(sample_text)
    print(words)