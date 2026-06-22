def sanitize_to_float(s):
    cleaned = ''.join(char for char in s if char.isdigit() or char == '.')
    if not cleaned or cleaned.count('.') > 1:
        return 0.0
    return float(cleaned)

if __name__ == '__main__':
    sample_input = "abc12.5xyz67"
    result = sanitize_to_float(sample_input)
    print(result)