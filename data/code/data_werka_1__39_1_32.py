import re

def extract_non_overlapping(text, regex_pattern):
    matches = []
    for match in re.finditer(regex_pattern, text):
        if not any(match.start() < m.end() and match.end() > m.start() for m in matches):
            matches.append(match)
    return [m.group() for m in matches]

if __name__ == '__main__':
    sample_text = "apple banana apple orange apple"
    pattern = r"apple"
    result = extract_non_overlapping(sample_text, pattern)
    print(result)