class StringProcessor:
    def remove_spaces(self, input_string):
        return input_string.replace(" ", "")

if __name__ == '__main__':
    processor = StringProcessor()
    sample_input = "Hello World"
    print(processor.remove_spaces(sample_input))