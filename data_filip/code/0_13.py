import re

def extract_floats(text):
    pattern = r'-?\d+(?:\.\d+)?'
    matches = re.findall(pattern, text)
    return [float(num) for num in matches]

if __name__ == '__main__':
    sample_string = "The temperature dropped to -5.5 degrees while the pressure rose to 101.3 and 42 units of force were applied. Ignore text99abc."
    result = extract_floats(sample_string)
    print(result)