import re

def extract_digits_to_tuple(mixed_string):
    digits = re.findall(r'\d', mixed_string)
    return tuple(int(d) for d in digits)

if __name__ == '__main__':
    sample_input = "Order #A42-B9: shipped 2023-12-05"
    result = extract_digits_to_tuple(sample_input)
    print(result)