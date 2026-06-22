import unicodedata

def extract_digits(text: str) -> list[int]:
    digits = []
    for char in text:
        if unicodedata.category(char).startswith('Nd'):
            digits.append(int(char))
    return digits

if __name__ == '__main__':
    sample_text = "abc123xyz\u0664\u0665\u0666"
    result = extract_digits(sample_text)
    print(result)