import re

def extract_digits_to_tuple(mixed_string):
    digit_strings = re.findall(r'\d+', mixed_string)
    return tuple(int(d) for d in digit_strings)

if __name__ == '__main__':
    sample_input = "The year 2023 brought 42 changes for 90% of the 7 billion people."
    result = extract_digits_to_tuple(sample_input)
    print(result)