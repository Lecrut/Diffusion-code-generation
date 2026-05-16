class StringExtractor:
    def extract_substrings(self, text: str, delimiters: list[int]) -> list[str]:
        if not text:
            return []
        sorted_delimiters = sorted(list(set(delimiters)))
        substrings = []
        current_start = 0
        for delimiter_pos in sorted_delimiters:
            if current_start < delimiter_pos:
                substring = text[current_start:delimiter_pos]
                if substring:
                    substrings.append(substring)
            current_start = delimiter_pos
        if current_start < len(text):
            substring = text[current_start:]
            if substring:
                substrings.append(substring)
        return substrings
if __name__ == '__main__':
    extractor = StringExtractor()
    sample_text = "abc_def123ghi_jkl"
    sample_delimiters = [3, 7, 11]
    result = extractor.extract_substrings(sample_text, sample_delimiters)
    print(result)