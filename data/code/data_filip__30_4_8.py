def decimal_to_padded_binary(decimal_value, bit_length):
    if decimal_value < 0 or decimal_value >= (1 << bit_length):
        raise ValueError("Value out of range for given bit length")
    return format(decimal_value, '0{}b'.format(bit_length))

if __name__ == '__main__':
    print(decimal_to_padded_binary(5, 8))
    print(decimal_to_padded_binary(255, 16))
    print(decimal_to_padded_binary(0, 4))
    print(decimal_to_padded_binary(10, 5))