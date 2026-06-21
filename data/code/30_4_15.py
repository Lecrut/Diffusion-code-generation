def decimal_to_fixed_binary(value, bit_length):
    if bit_length <= 0:
        raise ValueError("Bit length must be positive")
    if value < 0 or value >= (1 << bit_length):
        raise ValueError(f"Value {value} out of range for {bit_length} bits")
    return format(value, f'0{bit_length}b')

if __name__ == '__main__':
    print(decimal_to_fixed_binary(5, 8))
    print(decimal_to_fixed_binary(10, 4))
    print(decimal_to_fixed_binary(0, 5))