class StringExtractor:
    def __init__(self, input_string):
        self.input_string = input_string

    def extract_substrings(self, delimiter_positions):
        substrings = []
        start = 0
        for position in sorted(delimiter_positions):
            if start < position:
                substrings.append(self.input_string[start:position])
            start = position + 1
        if start < len(self.input_string):
            substrings.append(self.input_string[start:])
        return substrings

if __name__ == '__main__':
    sample_string = "HelloWorldThisIsATest"
    delimiter_positions = [4, 8, 12]
    extractor = StringExtractor(sample_string)
    result = extractor.extract_substrings(delimiter_positions)
    print(result)