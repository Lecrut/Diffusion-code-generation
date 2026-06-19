import re

class PatternExtractor:
    DEFAULT_PATTERN = r'\b\w+\b'

    @staticmethod
    def extract_all_non_overlapping(text, pattern):
        return re.findall(pattern, text)

if __name__ == '__main__':
    sample_input = 'The quick brown fox jumps over the lazy dog.'
    pattern_to_find = PatternExtractor.DEFAULT_PATTERN
    extractor = PatternExtractor()
    result = extractor.extract_all_non_overlapping(sample_input, pattern_to_find)
    print(result)