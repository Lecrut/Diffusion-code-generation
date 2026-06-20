import unicodedata

def extract_digits(mixed_string):
    digits = []
    for char in mixed_string:
        if char.isdigit():
            digits.append(int(char))
    return digits

if __name__ == '__main__':
    sample_text = "Order 58-Δ9αβγ3.0"
    result = extract_digits(sample_text)
    print(result)