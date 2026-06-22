class StringProcessor:
    DEFAULT_INPUT = ["apple", "banana", "", "cherry"]

    @staticmethod
    def get_first_letter(s):
        return s[0] if s else ''

if __name__ == '__main__':
    processor = StringProcessor()
    sample_values = StringProcessor.DEFAULT_INPUT
    for value in sample_values:
        print(processor.get_first_letter(value))