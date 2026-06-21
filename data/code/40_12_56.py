def extract_first_alpha(s):
    ALPHABET_START = ord('A')
    ALPHABET_END = ord('Z')
    alphabet_set = set(range(ALPHABET_START, ALPHABET_END + 1)) | set(range(ord('a'), ord('z') + 1))
    
    for char in s:
        if ord(char) in alphabet_set:
            return char
    raise ValueError("No alphabetic character found")

if __name__ == '__main__':
    sample_values = [
        "456def",
        "!@#ghi",
        "   jkl",
        "7890mno",
        ""
    ]
    for value in sample_values:
        try:
            print(extract_first_alpha(value))
        except ValueError as e:
            print(e)