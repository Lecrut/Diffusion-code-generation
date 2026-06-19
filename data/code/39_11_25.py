class StringExtractor:
    def extract_substrings(self, text: str, delimiters: list[int]) -> list[str]:
        if not self._validate_input(text, delimiters):
            return []
        
        sorted_delimiters = sorted(list(set(delimiters)))
        substrings = []
        current_start = 0
        
        for delimiter_pos in sorted_delimiters:
            if current_start < delimiter_pos:
                substring = text[current_start:delimiter_pos]
                substrings.append(substring)
            current_start = delimiter_pos
        
        if current_start < len(text):
            substring = text[current_start:]
            substrings.append(substring)
        
        return substrings
    
    def _validate_input(self, text: str, delimiters: list[int]) -> bool:
        if not isinstance(text, str):
            return False
        if not all(isinstance(pos, int) and pos >= 0 for pos in delimiters):
            return False
        if any(pos > len(text) for pos in delimiters):
            return False
        return True

if __name__ == '__main__':
    extractor = StringExtractor()
    text = "HelloWorld"
    delimiters = [5, 10]
    result = extractor.extract_substrings(text, delimiters)
    print(result)