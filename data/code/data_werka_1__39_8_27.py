import re

def find_patterns_in_string(input_string, patterns):
    result = {}
    for pattern in patterns:
        matches = re.findall(pattern, input_string)
        result[pattern] = matches
    return result

if __name__ == '__main__':
    sample_string = "The quick brown fox jumps over the lazy dog. 1234567890"
    sample_patterns = [r'\b\w{5}\b', r'\d+', r'[aeiou]']
    print(find_patterns_in_string(sample_string, sample_patterns))