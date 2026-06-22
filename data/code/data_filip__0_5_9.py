import unicodedata

def extract_digits(s: str) -> list:
    digits = []
    for char in s:
        if char.isdigit():
            digits.append(unicodedata.digit(char))
    return digits

if __name__ == '__main__':
    sample_text = "Hello 123, world! 45 6789. Unicode: ① ② ③ ❿ 𝟘"
    result = extract_digits(sample_text)
    print(result)