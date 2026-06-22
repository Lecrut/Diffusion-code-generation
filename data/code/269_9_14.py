import re

def extract_punctuation(text):
    punctuation = []
    for match in re.finditer(r'\W+', text):
        punctuation.extend(match.group(0))
    return punctuation

if __name__ == '__main__':
    sample_string = "This is a test, to check if the function works correctly."
    result = extract_punctuation(sample_string)
    print(result)