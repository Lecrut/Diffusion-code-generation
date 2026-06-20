import re

def extract_floats(text):
    pattern = r'[-+]?\d*\.?\d+'
    matches = re.findall(pattern, text)
    floats = []
    for match in matches:
        try:
            floats.append(float(match))
        except ValueError:
            continue
    return floats

if __name__ == '__main__':
    sample_text = "The temperature is -3.5 degrees, and the pressure is 101.3 hPa, but the noise is 123abc456.78xyz!"
    result = extract_floats(sample_text)
    print(result)