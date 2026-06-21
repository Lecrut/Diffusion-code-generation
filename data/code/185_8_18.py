def extract_numbers(text):
    import re
    matches = re.findall(r'-?\d+\.\d+|\b\d+', text)
    return [float(match) for match in matches if match.replace('.', '', 1).isdigit()]

if __name__ == '__main__':
    sample_text = "There are 42 apples and 3.14159 pi."
    print(extract_numbers(sample_text))