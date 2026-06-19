import re
PATTERN = '\\b\\w{5}\\b'

def extract_non_overlapping_occurrences(input_string, pattern):
    return re.findall(pattern, input_string)

class TextProcessor:

    def __init__(self, text):
        self.text = text

    def find_all_occurrences(self, pattern):
        return re.findall(pattern, self.text)
if __name__ == '__main__':
    sample_input = 'The quick brown fox jumps over the lazy dog.'
    result_function = extract_non_overlapping_occurrences(sample_input, PATTERN)
    processor = TextProcessor(sample_input)
    result_class = processor.find_all_occurrences(PATTERN)
    print('Function Result:', result_function)
    print('Class Result:', result_class)