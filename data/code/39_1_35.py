import re

def extract_non_overlapping_occurrences(text, pattern):
    matches = []
    for match in re.finditer(pattern, text):
        matches.append(match.group())
    return matches

if __name__ == '__main__':
    sample_text = "Hello world! Hello everyone!"
    search_pattern = r"Hello"
    found_occurrences = extract_non_overlapping_occurrences(sample_text, search_pattern)
    print(found_occurrences)