def validate_and_convert_to_hex(binary_str):
    valid_chars = set('01')
    if not all(c in valid_chars for c in binary_str):
        raise ValueError("Invalid binary character found")
    decimal_value = int(binary_str, 2)
    hex_value = hex(decimal_value)
    return hex_value

if __name__ == '__main__':
    sample_valid = "10101011"
    sample_invalid = "10201"

    print(validate_and_convert_to_hex(sample_valid))

    try:
        validate_and_convert_to_hex(sample_invalid)
    except ValueError as e:
        print(str(e))