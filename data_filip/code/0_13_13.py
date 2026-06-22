import re

def extract_floats(text):
    pattern = r'-?\d+\.\d+|-?\d+'
    matches = re.findall(pattern, text)
    results = [float(m) for m in matches]
    return results

if __name__ == '__main__':
    sample_text = "Temperature: 23.5°C, Pressure: -101.325kPa, Count: 42"
    values = extract_floats(sample_text)
    print(values)