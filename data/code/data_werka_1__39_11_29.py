class StringExtractor:
    DELIMITER_START = 0

    @staticmethod
    def _sort_and_filter_delimiters(delimiters):
        return sorted(list(set(delimiters)))

    def extract_substrings(self, text: str, delimiters: list[int]) -> list[str]:
        if not text:
            return []
        
        sorted_delimiters = self._sort_and_filter_delimiters(delimiters)
        substrings = []
        current_start = StringExtractor.DELIMITER_START
        
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
    sample_text = "HelloWorld"
    sample_delimiters = [5, 10]
    print(extractor.extract_substrings(sample_text, sample_delimiters))