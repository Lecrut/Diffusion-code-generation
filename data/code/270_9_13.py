class StringProcessor:
    @staticmethod
    def remove_spaces(input_string):
        return input_string.replace(" ", "")

if __name__ == '__main__':
    sample_input = "Hello World"
    processor = StringProcessor()
    print(processor.remove_spaces(sample_input))