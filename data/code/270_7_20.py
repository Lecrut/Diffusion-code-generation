class StringProcessor:
    def __init__(self):
        self.translation_table = str.maketrans('', '', ' ')

    def remove_spaces(self, s):
        return s.translate(self.translation_table)

if __name__ == '__main__':
    processor = StringProcessor()
    sample_string = "Hello, World! This is a test."
    result = processor.remove_spaces(sample_string)
    print(result)