def sanitize_to_float(mixed_string):
    digits_only = ''.join(char for char in mixed_string if char.isdigit() or char == '.')
    if not digits_only or digits_only.count('.') > 1:
        digits_only = digits_only.replace('.', '', digits_only.count('.') - 1)
    if not digits_only:
        return 0.0
    if digits_only.startswith('.') or digits_only.endswith('.'):
        if digits_only.startswith('.'):
            digits_only = '0' + digits_only
        if digits_only.endswith('.'):
            digits_only = digits_only + '0'
    return float(digits_only)

if __name__ == '__main__':
    test_cases = ["abc123.45def", "x9y8z7.6", "...111...", "no_digits_here", ".50"]
    for test in test_cases:
        result = sanitize_to_float(test)
        print(result)