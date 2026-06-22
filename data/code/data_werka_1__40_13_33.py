def extract_first_alpha(s):
    for char in s:
        if char.isalpha():
            return char
    return None

if __name__ == '__main__':
    sample_values = [
        "123abc",
        "!@#Hello",
        "4567890",
        "NoLeadingDigits",
        "   LeadingSpaces",
        ""
    ]
    
    for value in sample_values:
        print(extract_first_alpha(value))