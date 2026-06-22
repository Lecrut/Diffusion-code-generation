import re

def extract_digit_sequences(s):
    matches = re.findall(r'\d+', s)
    return [int(match) for match in matches]

if __name__ == '__main__':
    sample1 = "abc123def45ghi6"
    sample2 = "no digits here"
    sample3 = "100 apples and 200 oranges"
    print(extract_digit_sequences(sample1))
    print(extract_digit_sequences(sample2))
    print(extract_digit_sequences(sample3))