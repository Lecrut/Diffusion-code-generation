import re

def find_substrings_by_patterns(input_string, patterns):
    result = {}
    for pattern in patterns:
        matches = re.findall(pattern, input_string)
        result[pattern] = matches
    return result

if __name__ == '__main__':
    sample_string = "The quick brown fox jumps over the lazy dog. 1234567890"
    sample_patterns = [r'\b\w{5}\b', r'\d+', r'[aeiou]{2}']
    print(find_substrings_by_patterns(sample_string, sample_patterns))