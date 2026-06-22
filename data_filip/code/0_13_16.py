import re

def extract_floats(text):
    pattern = r'-?\d+\.\d+|-?\d+'
    matches = re.findall(pattern, text)
    return [float(num) for num in matches]

if __name__ == '__main__':
    sample_text = "The value is 12.34 and the discount is -5.67 or just 8. The noise 99a is ignored."
    result = extract_floats(sample_text)
    print(result)