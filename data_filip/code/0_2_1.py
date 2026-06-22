import re

def extract_digits_to_tuple(text):
    digits = re.findall(r'\d', text)
    return tuple(int(d) for d in digits)

if __name__ == '__main__':
    sample_string = "Order #42-ABC: 100 units of item 7, then 3 more."
    result = extract_digits_to_tuple(sample_string)
    print(result)