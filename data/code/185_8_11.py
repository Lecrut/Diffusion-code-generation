def extract_numbers(text):
    import re
    return [float(num) for num in re.findall(r'\b\d+\.\d+|\b\d+', text)]

if __name__ == '__main__':
    sample_text = "There are 42 apples and 3.14159 pies."
    print(extract_numbers(sample_text))