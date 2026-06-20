import re

def extract_digits_as_int_tuple(text):
    return tuple(int(match) for match in re.findall(r'\d+', text))

if __name__ == '__main__':
    sample_string = "abc123def45gh6789"
    result = extract_digits_as_int_tuple(sample_string)
    print(result)