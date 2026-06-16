import re
def extract_first_letters(text):
    return re.sub(r'\b\w', lambda m: m.group(0)[0], text)
if __name__ == '__main__':
    sample_string = "This is a sample string for testing regex and word extraction"
    result = extract_first_letters(sample_string)
    print(result)