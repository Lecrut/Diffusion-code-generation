def decimal_to_padded_binary(value, bit_length):
    if bit_length <= 0:
        raise ValueError("bit_length must be positive")
    if value < 0:
        raise ValueError("value cannot be negative")
    if value >= (1 << bit_length):
        raise ValueError("value exceeds the capacity of the specified bit length")
    return format(value, f'0{bit_length}b')

if __name__ == '__main__':
    print(decimal_to_padded_binary(42, 8))
    print(decimal_to_padded_binary(0, 4))
    print(decimal_to_padded_binary(255, 16))
    print(decimal_to_padded_binary(1024, 12))