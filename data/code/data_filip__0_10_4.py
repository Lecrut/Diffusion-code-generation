import re

def extract_digits_as_integers(text: str) -> list[int]:
    if not text:
        return []
    digit_strings = re.findall(r'\d+', text)
    return [int(num) for num in digit_strings]

if __name__ == '__main__':
    sample_input = "User ID 42 logged in at 14:30 and accessed file 998.txt."
    result = extract_digits_as_integers(sample_input)
    print(result)