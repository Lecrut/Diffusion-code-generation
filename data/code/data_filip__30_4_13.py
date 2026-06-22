def decimal_to_fixed_width_binary(decimal_value, bit_length):
    if decimal_value < 0 or decimal_value >= (1 << bit_length):
        raise ValueError("Value out of range for given bit length")
    return format(decimal_value, f'0{bit_length}b')

if __name__ == '__main__':
    print(decimal_to_fixed_width_binary(5, 8))
    print(decimal_to_fixed_width_binary(255, 8))
    print(decimal_to_fixed_width_binary(10, 4))