def to_upper(s: str) -> str:
    return ''.join(char.upper() for char in s)

def to_lower(s: str) -> str:
    return ''.join(char.lower() for char in s)

def validate_string(s: str) -> bool:
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    return True

if __name__ == '__main__':
    sample_string = "HeLlO wOrLd"
    validate_string(sample_string)
    
    upper_result = to_upper(sample_string)
    lower_result = to_lower(sample_string)
    
    print(f"Original: {sample_string}")
    print(f"Uppercase: {upper_result}")
    print(f"Lowercase: {lower_result}")