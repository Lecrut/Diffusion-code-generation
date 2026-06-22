def sanitize_to_float(s):
    digits = [c for c in s if c.isdigit()]
    result_str = ''.join(digits)
    if result_str:
        return float(result_str)
    return 0.0

if __name__ == '__main__':
    sample_strings = [
        "123.45",
        "abc123xyz",
        "",
        "no digits here",
        "9.99a1b2"
    ]
    
    for s in sample_strings:
        print(sanitize_to_float(s))