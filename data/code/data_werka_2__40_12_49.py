def extract_first_alpha(s):
    first_alpha = None
    for char in s:
        if char.isalpha():
            first_alpha = char
            break
    if first_alpha is None:
        raise ValueError("No alphabetic character found")
    return first_alpha

if __name__ == '__main__':
    sample_values = [
        "123abc",
        "!@#456def",
        "   ghi",
        "7890",
        ""
    ]
    for value in sample_values:
        try:
            print(extract_first_alpha(value))
        except ValueError as e:
            print(e)