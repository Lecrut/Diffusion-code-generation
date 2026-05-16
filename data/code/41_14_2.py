def to_lower(s: str) -> str:
    return s.lower()
def to_upper(s: str) -> str:
    return s.upper()
def to_title(s: str) -> str:
    return s.title()
if __name__ == '__main__':
    sample_string = "HeLlO wOrLd ExAmPle"
    lower_result = to_lower(sample_string)
    upper_result = to_upper(sample_string)
    title_result = to_title(sample_string)
    print(f"Original: {sample_string}")
    print(f"Lowercase: {lower_result}")
    print(f"Uppercase: {upper_result}")
    print(f"Title Case: {title_result}")