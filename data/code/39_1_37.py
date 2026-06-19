import re

def extract_non_overlapping_occurrences(input_string, pattern):
    return re.findall(pattern, input_string)

if __name__ == '__main__':
    sample_input = "abracadabra"
    sample_pattern = r"abra"
    result = extract_non_overlapping_occurrences(sample_input, sample_pattern)
    print(result)