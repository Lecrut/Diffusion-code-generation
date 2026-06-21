class StringProcessor:
    @staticmethod
    def remove_spaces(input_string):
        return input_string.replace(" ", "")

if __name__ == '__main__':
    sample_input = "  This is   a different example string with various spaces.  "
    processor = StringProcessor()
    result = processor.remove_spaces(sample_input)
    print(result)