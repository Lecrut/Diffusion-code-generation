import re

def extract_floats(text):
    pattern = r'-?\d+\.\d+|-?\d+'
    matches = re.findall(pattern, text)
    return [float(match) for match in matches]

if __name__ == '__main__':
    sample_string = "The temperature is 23.5 degrees, and the pressure dropped to -10.2 units while the count was 500. It seems 3.14159 is a good approximation, but 7 is not a decimal."
    result = extract_floats(sample_string)
    print(result)