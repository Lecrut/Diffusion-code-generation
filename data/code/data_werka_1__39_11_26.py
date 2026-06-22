class StringExtractor:
    def __init__(self):
        self.delimiter_map = {}

    def add_delimiters(self, delimiters):
        for index, pos in enumerate(delimiters):
            self.delimiter_map[pos] = index

    def extract_substrings(self, text: str) -> list[str]:
        if not text:
            return []

        sorted_positions = sorted(self.delimiter_map.keys())
        substrings = []
        current_start = 0

        for position in sorted_positions:
            substring = text[current_start:position]
            if substring:
                substrings.append(substring)
            current_start = position

        if current_start < len(text):
            substring = text[current_start:]
            if substring:
                substrings.append(substring)

        return substrings

if __name__ == '__main__':
    extractor = StringExtractor()
    delimiters = [3, 7, 10]
    extractor.add_delimiters(delimiters)
    input_text = "HelloWorldThisIsATest"
    result = extractor.extract_substrings(input_text)
    print(result)