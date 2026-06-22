class StringProcessor:
    SPACE = " "

    @staticmethod
    def remove_spaces(input_string):
        return input_string.replace(StringProcessor.SPACE, "")

if __name__ == '__main__':
    sample_input = "Hello World"
    processor = StringProcessor()
    print(processor.remove_spaces(sample_input))