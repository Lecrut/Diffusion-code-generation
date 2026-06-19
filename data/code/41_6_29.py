class TitleCaseConverter:
    def __init__(self, input_strings):
        self.input_strings = input_strings

    def convert(self):
        return [s.title() for s in self.input_strings]

if __name__ == '__main__':
    sample_strings = ["hello world", "PYTHON programming", "this is a TEST"]
    converter = TitleCaseConverter(sample_strings)
    title_cased_strings = converter.convert()
    print(title_cased_strings)