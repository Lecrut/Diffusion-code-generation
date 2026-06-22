def extract_first_alpha(s):
    for char in s:
        if char.isalpha():
            return char
    raise ValueError("No alphabetic character found")

if __name__ == '__main__':
    sample_values = [
        "987xyz",
        "(^&*())UVW",
        "qrst123456",
        "LMNopq",
        "789"
    ]
    for value in sample_values:
        try:
            print(extract_first_alpha(value))
        except ValueError as e:
            print(e)