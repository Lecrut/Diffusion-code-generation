def decimal_to_fixed_binary(value, bit_length):
    if bit_length < 0:
        raise ValueError("bit_length cannot be negative")
    if value < 0:
        raise ValueError("value cannot be negative for this conversion")
    if value.bit_length() > bit_length:
        raise ValueError(f"value {value} exceeds {bit_length} bits")
    return format(value, f'0{bit_length}b')

if __name__ == '__main__':
    sample_value = 42
    sample_bits = 8
    result = decimal_to_fixed_binary(sample_value, sample_bits)
    print(result)
    sample_value_large = 255
    sample_bits_large = 10
    result_large = decimal_to_fixed_binary(sample_value_large, sample_bits_large)
    print(result_large)
    try:
        decimal_to_fixed_binary(256, 8)
    except ValueError as e:
        print(e)