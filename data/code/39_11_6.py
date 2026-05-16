class StringExtractor:
    def extract_non_overlapping(self, text: str, delimiters: list[int]) -> list[str]:
        if not delimiters:
            return [text]
        sorted_delimiters = sorted(list(set(delimiters)))
        start = 0
        extracted_substrings = []
        for delim in sorted_delimiters:
            if start < delim:
                extracted_substrings.append(text[start:delim])
            start = delim
        if start < len(text):
            extracted_substrings.append(text[start:])
        return extracted_substrings
if __name__ == '__main__':
    extractor = StringExtractor()
    sample_text = "apple,banana,cherry,date"
    sample_delimiters = [5, 12, 19]
    result = extractor.extract_non_overlapping(sample_text, sample_delimiters)
    print(result)