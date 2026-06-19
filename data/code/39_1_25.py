import re
PATTERN = '\\b\\w{5}\\b'

def extract_non_overlapping_occurrences(input_string, pattern):
    return re.findall(pattern, input_string)
if __name__ == '__main__':
    sample_input = 'The quick brown fox jumps over the lazy dog.'
    result = extract_non_overlapping_occurrences(sample_input, PATTERN)
    print(result)