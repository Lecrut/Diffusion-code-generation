import re

def extract_digits_as_integers(text):
    matches = re.findall(r'\d+', text)
    return [int(match) for match in matches]

if __name__ == '__main__':
    sample_text = "abc123def45ghi6789jkl"
    result = extract_digits_as_integers(sample_text)
    print(result)