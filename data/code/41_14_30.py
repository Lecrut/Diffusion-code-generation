def is_valid_string(s):
    return isinstance(s, str)

def to_upper(s: str) -> str:
    if not is_valid_string(s):
        raise ValueError("Input must be a string")
    return ''.join([char.upper() for char in s])

def to_lower(s: str) -> str:
    if not is_valid_string(s):
        raise ValueError("Input must be a string")
    return ''.join([char.lower() for char in s])

if __name__ == '__main__':
    sample_string = "HeLlO wOrLd"
    print(f"Original: {sample_string}")
    print(f"Uppercase: {to_upper(sample_string)}")
    print(f"Lowercase: {to_lower(sample_string)}")