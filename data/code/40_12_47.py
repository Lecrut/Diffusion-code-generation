def is_alpha(char):
    return char.isalpha()

def extract_first_alpha(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    
    for char in s:
        if is_alpha(char):
            return char
    
    raise ValueError("No alphabetic character found")

if __name__ == '__main__':
    sample_values = [
        "123abc",
        "!@#456def",
        "   ghi",
        "7890",
        "",
        "noalpha123",
        "anotherTest!@#"
    ]
    
    for value in sample_values:
        try:
            print(extract_first_alpha(value))
        except ValueError as e:
            print(e)