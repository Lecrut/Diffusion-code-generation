class StringExtractor:
    def __init__(self, input_string):
        self.input_string = input_string

    def extract_substrings(self, delimiter_positions):
        substrings = []
        start = 0
        for pos in delimiter_positions:
            if pos > start:
                substrings.append(self.input_string[start:pos])
            start = pos + 1
        if start < len(self.input_string):
            substrings.append(self.input_string[start:])
        return substrings

if __name__ == '__main__':
    input_str = "HelloWorldThisIsATest"
    delimiters = [4, 8, 12]
    extractor = StringExtractor(input_str)
    result = extractor.extract_substrings(delimiters)
    print(result)