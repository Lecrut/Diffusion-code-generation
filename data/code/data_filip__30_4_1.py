def decimal_to_zero_padded_binary(decimal_value, bit_length):
    if decimal_value < 0:
        raise ValueError("Negative values are not supported")
    if decimal_value >= (1 << bit_length):
        raise ValueError("Value exceeds the specified bit length")
    binary_str = bin(decimal_value)[2:]
    return binary_str.zfill(bit_length)

if __name__ == '__main__':
    print(decimal_to_zero_padded_binary(5, 8))
    print(decimal_to_zero_padded_binary(255, 8))
    print(decimal_to_zero_padded_binary(0, 4))
    print(decimal_to_zero_padded_binary(10, 16))