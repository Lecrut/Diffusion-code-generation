def zero_padded_binary(decimal_value, bit_length):
    if bit_length < 0:
        raise ValueError("bit_length must be non-negative")
    if decimal_value < 0 or decimal_value >= (1 << bit_length):
        raise ValueError(f"decimal_value {decimal_value} is out of range for {bit_length}-bit representation")
    return format(decimal_value, f'0{bit_length}b')

if __name__ == '__main__':
    print(zero_padded_binary(5, 8))
    print(zero_padded_binary(255, 8))
    print(zero_padded_binary(0, 16))
    print(zero_padded_binary(1, 1))