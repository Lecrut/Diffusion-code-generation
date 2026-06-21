def extract_numbers(text):
    import re
    return [float(num) for num in re.findall(r'-?\d+\.\d+|\d+', text)]

if __name__ == '__main__':
    sample_text = "There are 42 apples and 3.141592653589793 pi."
    print(extract_numbers(sample_text))