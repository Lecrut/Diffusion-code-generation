def get_first_letter(s):
    if not isinstance(s, str) or not s:
        raise ValueError("Input must be a non-empty string")
    return s[0]

if __name__ == '__main__':
    sample_values = {
        "greeting": "Hello, World!",
        "company": "Alibaba Cloud",
        "language": "Python"
    }
    
    for key, value in sample_values.items():
        first_letter = get_first_letter(value)
        print(f"The first letter of '{value}' is: {first_letter}")