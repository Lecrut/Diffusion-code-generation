import re

def extract_all_non_overlapping(text, pattern):
    return re.findall(pattern, text)

if __name__ == '__main__':
    sample_input = "cat and dog in a hat. Cats like to play with the cat in the bag."
    pattern_to_find = r"\bcat\b"
    occurrences = extract_all_non_overlapping(sample_input, pattern_to_find)
    print(occurrences)