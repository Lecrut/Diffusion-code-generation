import re

def extract_floats(text):
    pattern = r'-?\d+\.?\d*|-\.\d+'
    matches = re.findall(pattern, text)
    return [float(m) for m in matches]

if __name__ == '__main__':
    sample_text = "Values are 3.14, -2.5, and 100 with noise like abc and 0.001"
    print(extract_floats(sample_text))