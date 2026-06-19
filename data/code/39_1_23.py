import re

def find_non_overlapping_matches(text, pattern):
    matches = []
    for match in re.finditer(pattern, text):
        if not any(match.start() < m.end() and match.end() > m.start() for m in matches):
            matches.append(match)
    return [m.group() for m in matches]

if __name__ == '__main__':
    sample_text = "apple banana apple orange apple"
    regex_pattern = r"apple"
    results = find_non_overlapping_matches(sample_text, regex_pattern)
    print(results)