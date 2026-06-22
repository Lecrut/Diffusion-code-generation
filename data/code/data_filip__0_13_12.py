import re

def extract_floats(text):
    pattern = r'-?\d+\.\d+|-?\d+'
    matches = re.findall(pattern, text)
    results = [float(match) for match in matches]
    return results

if __name__ == '__main__':
    sample_text = "Value is 42.5 and another one is -3.14, noise 100"
    values = extract_floats(sample_text)
    print(values)