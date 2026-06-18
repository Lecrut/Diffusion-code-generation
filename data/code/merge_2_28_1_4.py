import re
def extract_unique_animals(input_string: str) -> list[str]:
    pattern = r'\b[A-Za-z]+\b'
    matches = re.findall(pattern, input_string.lower())
    unique_set = set(matches)
    return [word.title() for word in sorted(unique_set)]
if __name__ == '__main__':
    sample_input = "lion Tiger lion tiger elephant ELEPHANT zebra ZEBRA"
    result = extract_unique_animals(sample_input)
    print(result)