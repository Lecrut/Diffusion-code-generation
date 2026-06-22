import re

def extract_floats(text):
    pattern = r'-?\d+\.?\d*'
    matches = re.findall(pattern, text)
    return [float(num) for num in matches if num != '.']

if __name__ == '__main__':
    sample_data = "Price is 10.5 dollars and -3.75 cents with noise 99abc"
    result = extract_floats(sample_data)
    print(result)