import re

def extract_floats(text):
    return [float(match) for match in re.finditer(r'-?\d+\.\d+|-?\d+', text)]

if __name__ == '__main__':
    sample_text = "Price is 100.5 and cost is -20 or 300. No text here."
    result = extract_floats(sample_text)
    print(result)