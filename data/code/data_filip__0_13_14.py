import re

def extract_floats(text):
    if not text:
        return []
    pattern = r'-?\d+(?:\.\d+)?'
    matches = re.findall(pattern, text)
    return [float(num) for num in matches if num]

if __name__ == '__main__':
    sample_input = "The sensor read 42.5 units, then dropped to -3.14, and finally stabilized at 100."
    result = extract_floats(sample_input)
    print(result)