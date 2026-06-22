import re

def extract_floats(text):
    pattern = r'-?\d+\.\d+|-?\d+'
    matches = re.findall(pattern, text)
    result = []
    for match in matches:
        try:
            value = float(match)
            result.append(value)
        except ValueError:
            continue
    return result

if __name__ == '__main__':
    sample_text = "The values are 12.5, -3.14, abc, 100, and .5."
    floats = extract_floats(sample_text)
    print(floats)