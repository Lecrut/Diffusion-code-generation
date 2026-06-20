import re

def extract_digits(text):
    return [int(match) for match in re.findall(r'\d+', text)]

if __name__ == '__main__':
    sample_text = "The temperature is 23 degrees, and the pressure is 1013 with 2 variations."
    result = extract_digits(sample_text)
    print(result)