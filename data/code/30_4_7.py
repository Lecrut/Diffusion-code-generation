def decimal_to_fixed_width_binary(decimal_value, bit_length):
    if decimal_value < 0:
        raise ValueError("Decimal value must be non-negative")
    if bit_length <= 0:
        raise ValueError("Bit length must be positive")
    binary_string = bin(decimal_value)[2:]
    if len(binary_string) > bit_length:
        raise ValueError("Decimal value exceeds the specified bit length")
    return binary_string.zfill(bit_length)

if __name__ == '__main__':
    print(decimal_to_fixed_width_binary(5, 8))
    print(decimal_to_fixed_width_binary(10, 8))
    print(decimal_to_fixed_width_binary(255, 8))
    print(decimal_to_fixed_width_binary(0, 4))
    print(decimal_to_fixed_width_binary(15, 4))