class StringProcessor:
    DELIMITER = ' '

    @staticmethod
    def find_first_word(s):
        index = s.find(StringProcessor.DELIMITER)
        return s[:index] if index != -1 else s

if __name__ == '__main__':
    processor = StringProcessor()
    sample_string = "The quick brown fox"
    print(processor.find_first_word(sample_string))