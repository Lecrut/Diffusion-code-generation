import re

def extract_digits_as_integers(text):
    return [int(match) for match in re.findall(r'\d+', text)]

if __name__ == '__main__':
    sample_text = "abc123def45ghi6789"
    result = extract_digits_as_integers(sample_text)
    print(result)