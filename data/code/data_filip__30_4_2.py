def decimal_to_fixed_binary(number: int, bit_length: int) -> str:
    binary_repr = bin(number)[2:]
    if len(binary_repr) > bit_length:
        binary_repr = binary_repr[-bit_length:]
    else:
        binary_repr = '0' * (bit_length - len(binary_repr)) + binary_repr
    return binary_repr

if __name__ == '__main__':
    print(decimal_to_fixed_binary(5, 8))
    print(decimal_to_fixed_binary(255, 12))
    print(decimal_to_fixed_binary(1, 4))