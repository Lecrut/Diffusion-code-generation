import re

def extract_non_overlapping_occurrences(input_string, pattern):
    return re.findall(pattern, input_string)
if __name__ == '__main__':
    sample_input = 'The rain in Spain falls mainly in the plain.'
    sample_pattern = '\\b\\w{5}\\b'
    result = extract_non_overlapping_occurrences(sample_input, sample_pattern)
    print(result)