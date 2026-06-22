import re

def find_patterns_in_string(input_string, patterns):
    pattern_dict = {}
    for pattern in patterns:
        matches = re.findall(pattern, input_string)
        pattern_dict[pattern] = matches
    return pattern_dict

if __name__ == '__main__':
    sample_string = "The rain in Spain falls mainly in the plain."
    sample_patterns = [r'\b\w+ain\b', r'\bin\b', r'\bS\w+\b']
    result = find_patterns_in_string(sample_string, sample_patterns)
    print(result)