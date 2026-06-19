class StringExtractor:

    def extract_substrings(self, text: str, delimiters: list[int]) -> list[str]:
        if not isinstance(text, str):
            raise ValueError('Input text must be a string')
        if not isinstance(delimiters, list) or not all((isinstance(d, int) for d in delimiters)):
            raise ValueError('Delimiters must be a list of integers')
        if len(text) == 0:
            return []
        sorted_delimiters = sorted(set(delimiters))
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
    sample_text = 'HelloWorld'
    sample_delimiters = [5, 10]
    result = extractor.extract_substrings(sample_text, sample_delimiters)
    print(result)