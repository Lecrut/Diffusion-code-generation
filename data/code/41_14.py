def to_lower(s):
    return s.lower()
def to_upper(s):
    return s.upper()
def to_title(s):
    return s.title()
if __name__ == '__main__':
    sample_string = "HeLlO wOrLd"
    print(f"Original: {sample_string}")
    print(f"Lowercase: {to_lower(sample_string)}")
    print(f"Uppercase: {to_upper(sample_string)}")
    print(f"Title Case: {to_title(sample_string)}")