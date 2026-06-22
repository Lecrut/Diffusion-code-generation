def extract_first_alpha(s):
    return next((char for char in s if char.isalpha()), None)

if __name__ == '__main__':
    sample_values = [
        "123abc",
        "!@#456def",
        "   ghi",
        "7890",
        ""
    ]
    for value in sample_values:
        result = extract_first_alpha(value)
        if result is None:
            print("No alphabetic character found")
        else:
            print(result)