import re

class PatternExtractor:
    DEFAULT_PATTERN = r"\b\w{5}\b"

    @staticmethod
    def extract_non_overlapping_occurrences(input_string, pattern=DEFAULT_PATTERN):
        return re.findall(pattern, input_string)

if __name__ == '__main__':
    sample_input = 'The quick brown fox jumps over the lazy dog.'
    result = PatternExtractor.extract_non_overlapping_occurrences(sample_input)
    print(result)