import re

def extract_digits(s: str) -> list[int]:
    return [int(match) for match in re.findall(r'\d+', s)]

if __name__ == '__main__':
    sample_input = "The code 123 is in file 456 with version 7890."
    result = extract_digits(sample_input)
    print(result)