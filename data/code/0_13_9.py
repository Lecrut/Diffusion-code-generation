import re

def extract_floats(text):
    pattern = r'-?\d+\.\d+|-?\d+'
    matches = re.findall(pattern, text)
    return [float(m) for m in matches]

if __name__ == '__main__':
    sample_text = "The values are 12.34, -5.6, 789, and not_a_number, 42.0"
    result = extract_floats(sample_text)
    print(result)