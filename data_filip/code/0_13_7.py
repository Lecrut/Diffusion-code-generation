import re

def extract_floats(text):
    pattern = r'-?\d+\.\d+|-?\d+'
    matches = re.findall(pattern, text)
    return [float(match) for match in matches]

if __name__ == '__main__':
    sample_text = "The temperature dropped to -4.5 degrees, from 30.1 earlier."
    result = extract_floats(sample_text)
    print(result)