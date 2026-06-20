def sanitize_to_float(text):
    digits = ''.join(char for char in text if char.isdigit() or char == '.')
    if not digits:
        return 0.0
    dot_count = digits.count('.')
    if dot_count == 0:
        return float(digits)
    if dot_count > 1:
        first_dot = digits.find('.')
        last_dot = digits.rfind('.')
        digits = digits[:first_dot] + digits[first_dot + 1:]
        if digits.find('.') == -1:
            return float(digits)
    try:
        return float(digits)
    except ValueError:
        return 0.0

if __name__ == '__main__':
    sample_data = ["abc12.34def", "!!!55.66!!!", "no_digits_here", "78.90xyz12.3"]
    for s in sample_data:
        result = sanitize_to_float(s)
        print(result)