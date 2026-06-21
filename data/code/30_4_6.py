def decimal_to_zero_padded_binary(decimal_value, bit_length):
    if decimal_value < 0:
        raise ValueError("Decimal value cannot be negative")
    if bit_length <= 0:
        raise ValueError("Bit length must be positive")
    max_value = (1 << bit_length) - 1
    if decimal_value > max_value:
        raise ValueError(f"Decimal value {decimal_value} exceeds maximum value {max_value} for {bit_length} bits")
    return format(decimal_value, f'0{bit_length}b')

if __name__ == '__main__':
    sample_decimal = 42
    sample_bit_length = 8
    result = decimal_to_zero_padded_binary(sample_decimal, sample_bit_length)
    print(result)
    
    sample_decimal_2 = 1024
    sample_bit_length_2 = 16
    result_2 = decimal_to_zero_padded_binary(sample_decimal_2, sample_bit_length_2)
    print(result_2)