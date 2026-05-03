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
    sample_text = "abc_def_ghi_jkl"
    sample_delimiters = [3, 7, 11]
    result = extractor.extract_substrings(sample_text, sample_delimiters)
    print(result)