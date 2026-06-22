import re

def find_patterns_in_string(input_string, patterns):
    result = {}
    for pattern in patterns:
        matches = re.findall(pattern, input_string)
        result[pattern] = matches
    return result

if __name__ == '__main__':
    sample_string = "The rain in Spain falls mainly in the plain."
    sample_patterns = [r'\b\w{5}\b', r'\bin\b', r'\bS\w+']
    print(find_patterns_in_string(sample_string, sample_patterns))