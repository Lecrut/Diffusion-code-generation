def decimal_to_binary_bit_length(value: int, bit_length: int) -> str:
    binary = bin(value)[2:]
    padding = bit_length - len(binary)
    if padding < 0:
        raise ValueError(f"Bit length {bit_length} is too small for value {value}")
    return '0' * padding + binary

if __name__ == '__main__':
    print(decimal_to_binary_bit_length(10, 8))
    print(decimal_to_binary_bit_length(255, 8))
    print(decimal_to_binary_bit_length(1, 4))