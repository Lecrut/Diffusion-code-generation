def binary_string_to_hex(binary_string):
    if not binary_string:
        return '0'
    normalized = binary_string.lstrip('0')
    if not normalized:
        return '0'
    decimal_value = int(normalized, 2)
    return format(decimal_value, 'x')

if __name__ == '__main__':
    test_cases = ['1101', '000101', '11111111', '0000', '1']
    for case in test_cases:
        result = binary_string_to_hex(case)
        print(f"{case} -> {result}")