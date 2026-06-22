import re

def extract_floats(text):
    pattern = r'-?\d+\.?\d*'
    matches = re.findall(pattern, text)
    result = []
    for match in matches:
        if match.strip().count('.') > 1:
            continue
        try:
            val = float(match)
            result.append(val)
        except ValueError:
            continue
    return result

if __name__ == '__main__':
    sample_input = "The temperature dropped from 72.5 to -10.3 degrees, while the noise level was 85.2. Ignore abc123 and xyz9.9.9."
    extracted_values = extract_floats(sample_input)
    print(extracted_values)