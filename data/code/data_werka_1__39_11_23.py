class StringExtractor:

    def extract_substrings(self, text: str, delimiters: list[int]) -> list[str]:
        if not text or not delimiters:
            return []
        sorted_delimiters = sorted(set(delimiters))
        substrings = []
        current_start = 0
        for delimiter_pos in sorted_delimiters:
            if current_start < delimiter_pos:
                substrings.append(text[current_start:delimiter_pos])
            current_start = delimiter_pos
        if current_start < len(text):
            substrings.append(text[current_start:])
        return substrings
if __name__ == '__main__':
    extractor = StringExtractor()
    text_sample = 'HelloWorld'
    delimiters_sample = [5, 7]
    result = extractor.extract_substrings(text_sample, delimiters_sample)
    print(result)