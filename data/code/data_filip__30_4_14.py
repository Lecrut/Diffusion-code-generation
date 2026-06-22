def decimal_to_fixed_width_binary(decimal_input, bit_length):
    binary_str = bin(decimal_input)[2:]
    if len(binary_str) > bit_length:
        raise ValueError("Input exceeds bit length")
    return binary_str.zfill(bit_length)

if __name__ == '__main__':
    result = decimal_to_fixed_width_binary(5, 8)
    print(result)
    
    result2 = decimal_to_fixed_width_binary(10, 4)
    print(result2)