class StringExtractor:

    def extract_substrings(self, text: str, delimiters: list[int]) -> list[str]:
        if not text or not delimiters:
            return []
        sorted_delimiters = sorted(delimiters)
        substrings = []
        current_start = 0
        for delimiter in sorted_delimiters:
            if current_start < delimiter:
                substring = text[current_start:delimiter]
                if substring:
                    substrings.append(substring)
                current_start = delimiter
        if current_start < len(text):
            substring = text[current_start:]
            if substring:
                substrings.append(substring)
        return substrings
if __name__ == '__main__':
    extractor = StringExtractor()
    sample_text = 'HelloWorldThisIsATest'
    sample_delimiters = [5, 10, 14]
    result = extractor.extract_substrings(sample_text, sample_delimiters)
    print(result)