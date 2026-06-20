import re

def extract_floats(text):
    pattern = r'-?\d+\.?\d*'
    matches = re.findall(pattern, text)
    return [float(m) for m in matches if m != '-' and m != '.']

if __name__ == '__main__':
    sample = "The values are 3.14, -2.7, 100, and also 42.0001 in the noise abc!@#"
    result = extract_floats(sample)
    print(result)