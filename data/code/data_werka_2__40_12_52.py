def is_alpha_character(char):
    return char.isalpha()

def extract_first_alpha(s):
    for char in s:
        if is_alpha_character(char):
            return char
    raise ValueError("No alphabetic character found")

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