import re

def extract_digits_to_tuple(mixed_string):
    matches = re.findall(r'\d+', mixed_string)
    return tuple(int(match) for match in matches)

if __name__ == '__main__':
    sample = "a1b2c3.5d7e8f"
    result = extract_digits_to_tuple(sample)
    print(result)