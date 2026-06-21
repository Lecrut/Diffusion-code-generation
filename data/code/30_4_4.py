def decimal_to_padded_binary(decimal_input, bit_length):
    binary_str = bin(decimal_input)[2:]
    padded_binary = binary_str.zfill(bit_length)
    return padded_binary

if __name__ == '__main__':
    result = decimal_to_padded_binary(42, 8)
    print(result)