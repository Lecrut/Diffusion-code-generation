import math

SQUARE_CHARS = {chr(i * i) for i in range(1, 26)}

def extract_square_chars(s):
    return ''.join(char for char in s if char in SQUARE_CHARS)

if __name__ == '__main__':
    sample_string = "a1b2c3d4e5f6g7h8i9j0k"
    print(extract_square_chars(sample_string))