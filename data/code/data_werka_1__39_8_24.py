import re

def find_patterns_in_string(s, patterns):
    result = {}
    for pattern in patterns:
        matches = re.findall(pattern, s)
        result[pattern] = matches
    return result

if __name__ == '__main__':
    sample_string = "The rain in Spain falls mainly in the plain."
    sample_patterns = [r'\b\w+ain\b', r'\bS\w+', r'\bin\b']
    print(find_patterns_in_string(sample_string, sample_patterns))