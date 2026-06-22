import re

def extract_floats(text):
    pattern = r'-?\d+\.?\d*'
    matches = re.findall(pattern, text)
    results = []
    for match in matches:
        if match.endswith('.') and match.count('.') == 1 and len(match) == 1:
            continue
        if match == '.' or match == '-':
            continue
        try:
            results.append(float(match))
        except ValueError:
            continue
    return results

if __name__ == '__main__':
    sample_string = "The temperature is 23.5 degrees, but yesterday it was -5.2 or just 0. and noise like 123abc.456 and 999.9999."
    extracted_values = extract_floats(sample_string)
    print(extracted_values)