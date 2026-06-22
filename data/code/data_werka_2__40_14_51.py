def get_first_letter(s):
    if not isinstance(s, str) or len(s) == 0:
        raise ValueError("Input must be a non-empty string")
    return s[0]

if __name__ == '__main__':
    sample_strings = {
        "greeting": "Hello, World!",
        "company": "Alibaba Cloud",
        "language": "Python"
    }
    
    for key, value in sample_strings.items():
        try:
            first_letter = get_first_letter(value)
            print(f"The first letter of '{value}' is: {first_letter}")
        except ValueError as e:
            print(e)