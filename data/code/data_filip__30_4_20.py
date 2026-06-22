def decimal_to_fixed_width_binary(decimal_value, bit_length):
    binary_str = bin(decimal_value & ((1 << bit_length) - 1))[2:]
    padded_binary = binary_str.zfill(bit_length)
    return padded_binary

if __name__ == '__main__':
    result = decimal_to_fixed_width_binary(10, 8)
    print(result)
    result2 = decimal_to_fixed_width_binary(255, 8)
    print(result2)
    result3 = decimal_to_fixed_width_binary(7, 4)
    print(result3)