class StringProcessor:
    @staticmethod
    def remove_spaces(s):
        return s.translate(str.maketrans('', '', ' '))

if __name__ == '__main__':
    processor = StringProcessor()
    sample_string = "Hello, World! This is a test."
    result = processor.remove_spaces(sample_string)
    print(result)