import re

def extract_floats(text):
    pattern = r'\d+\.\d+|\d+'
    matches = re.findall(pattern, text)
    return [float(match) for match in matches]

if __name__ == '__main__':
    text = "Value is 3.14 and count is 42. Also -10 and 0.5."
    result = extract_floats(text)
    print(result)