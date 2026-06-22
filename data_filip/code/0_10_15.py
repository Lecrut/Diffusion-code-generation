import re

def extract_digits(text):
    return [int(x) for x in re.findall(r'\d+', text)]

if __name__ == '__main__':
    sample_string = "The price is 42 dollars and 15 cents, total 57 units."
    result = extract_digits(sample_string)
    print(result)