def extract_numbers(text):
    import re
    numbers = re.findall(r'\b\d+\.\d+|\b\d+', text)
    return [float(num) for num in numbers]

if __name__ == '__main__':
    sample_text = "There are 42 apples and 3.14159 pi."
    print(extract_numbers(sample_text))