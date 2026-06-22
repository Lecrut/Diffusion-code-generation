import re

def extract_digits_to_tuple(mixed_string: str) -> tuple:
    digits = re.findall(r'\d', mixed_string)
    return tuple(int(d) for d in digits)

if __name__ == '__main__':
    sample_data = "Order#99-Alpha2-Beta123-End45"
    result = extract_digits_to_tuple(sample_data)
    print(result)