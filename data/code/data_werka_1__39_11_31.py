class StringExtractor:

    def __init__(self, text: str):
        self.text = text

    def extract_substrings(self, delimiters: list[int]) -> list[str]:
        if not self.text or not delimiters:
            return []
        sorted_delimiters = sorted(delimiters)
        substrings = []
        current_start = 0
        for delimiter_pos in sorted_delimiters:
            substring = self.text[current_start:delimiter_pos]
            if substring:
                substrings.append(substring)
            current_start = delimiter_pos
        final_substring = self.text[current_start:]
        if final_substring:
            substrings.append(final_substring)
        return substrings
if __name__ == '__main__':
    sample_text = 'HelloWorldThisIsATest'
    sample_delimiters = [5, 10, 14]
    extractor = StringExtractor(sample_text)
    result = extractor.extract_substrings(sample_delimiters)
    print(result)