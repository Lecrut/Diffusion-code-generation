import re

def extract_digits(string):
    return [int(match) for match in re.findall(r'\d+', string)]

if __name__ == '__main__':
    sample_strings = [
        "abc123def456",
        "no digits here",
        "123",
        "a1b2c3",
        "100hello200world300",
        "  456  789  ",
        "test123test456test789test"
    ]
    for s in sample_strings:
        print(extract_digits(s))