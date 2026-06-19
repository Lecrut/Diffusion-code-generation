def is_valid_string(s):
    return isinstance(s, str)

def to_lower(s):
    if not is_valid_string(s):
        raise ValueError("Input must be a string")
    return ''.join(chr(c | 0x20) if 'A' <= chr(c) <= 'Z' else chr(c) for c in ord(char) for char in s)

def to_upper(s):
    if not is_valid_string(s):
        raise ValueError("Input must be a string")
    return ''.join(chr(c & ~0x20) if 'a' <= chr(c) <= 'z' else chr(c) for c in ord(char) for char in s)

if __name__ == '__main__':
    sample_string = "HeLlO wOrLd"
    print(f"Original: {sample_string}")
    print(f"Uppercase: {to_upper(sample_string)}")
    print(f"Lowercase: {to_lower(sample_string)}")