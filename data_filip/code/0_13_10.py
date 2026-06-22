import re

def extract_floats(text):
    pattern = r'-?\d+\.\d+|-?\d+'
    matches = re.findall(pattern, text)
    return [float(m) for m in matches]

if __name__ == '__main__':
    sample_text = "Value is 12.34, another is -5, noise 12abc34.56"
    result = extract_floats(sample_text)
    print(result)