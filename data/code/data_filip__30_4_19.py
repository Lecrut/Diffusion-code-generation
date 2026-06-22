def decimal_to_binary_padded(value: int, bit_length: int) -> str:
    if bit_length < 0 or value < 0:
        raise ValueError("Value and bit_length must be non-negative")
    if value.bit_length() > bit_length:
        raise ValueError(f"Value {value} exceeds {bit_length} bits")
    return format(value, f'0{bit_length}b')

if __name__ == '__main__':
    print(decimal_to_binary_padded(5, 8))
    print(decimal_to_binary_padded(0, 4))
    print(decimal_to_binary_padded(255, 8))