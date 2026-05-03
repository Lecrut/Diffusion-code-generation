class StringExtractor:
    def extract_substrings(self, text, delimiters):
        if not delimiters:
            return [text]
        sorted_delimiters = sorted(delimiters)
        substrings = []
        start = 0
        for delim in sorted_delimiters:
            if start < delim:
                substrings.append(text[start:delim])
            start = delim
        if start < len(text):
            substrings.append(text[start:])
        return substrings
if __name__ == '__main__':
    extractor = StringExtractor()
    sample_text = "apple,banana,cherry,date"
    sample_delimiters = [5, 7, 13, 19]
    result = extractor.extract_substrings(sample_text, sample_delimiters)
    print(result)