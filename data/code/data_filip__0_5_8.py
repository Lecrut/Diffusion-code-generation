import unicodedata

def extract_digits(input_string: str) -> list[int]:
    digits = []
    for char in input_string:
        if char.isdigit():
            digits.append(int(char))
    return digits

if __name__ == '__main__':
    sample_text = "abc123€567©890"
    result = extract_digits(sample_text)
    print(result)