import re

def extract_numeric_substrings(text):
    pattern = r'-?\b\d+\.?\d*\b|-\d+\.\d+|\b\d+\b'
    matches = re.findall(r'-?\d+\.?\d*', text)
    result = []
    for match in matches:
        try:
            if '.' in match:
                result.append(float(match))
            else:
                result.append(float(match))
        except ValueError:
            continue
    return result

if __name__ == '__main__':
    sample_text = "The temperature was -3.14 degrees, and the pressure is 101.3 kPa. Also 42 and 0.005."
    print(extract_numeric_substrings(sample_text))