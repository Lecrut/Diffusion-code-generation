def extract_first_alpha(s):
    for char in s:
        if char.isalpha():
            return char
    raise ValueError("No alphabetic character found")

if __name__ == '__main__':
    sample_values = [
        "123abc",
        "!@#Hello",
        "4567890",
        "Python3.8",
        "no_numbers_here"
    ]
    
    for value in sample_values:
        try:
            print(extract_first_alpha(value))
        except ValueError as e:
            print(e)