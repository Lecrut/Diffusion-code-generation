def to_zero_padded_binary(value, bit_length):
    if bit_length < 0:
        raise ValueError("Bit length cannot be negative")
    if value < 0:
        raise ValueError("Negative values are not supported for this conversion")
    max_value = (1 << bit_length) - 1
    if value > max_value:
        raise ValueError(f"Value {value} exceeds maximum of {max_value} for {bit_length} bits")
    binary_string = format(value, 'b')
    return binary_string.zfill(bit_length)

if __name__ == '__main__':
    sample_value_1 = 42
    sample_bits_1 = 8
    print(to_zero_padded_binary(sample_value_1, sample_bits_1))
    
    sample_value_2 = 5
    sample_bits_2 = 4
    print(to_zero_padded_binary(sample_value_2, sample_bits_2))
    
    sample_value_3 = 255
    sample_bits_3 = 8
    print(to_zero_padded_binary(sample_value_3, sample_bits_3))