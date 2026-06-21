def to_zero_padded_binary(value, length):
    if length < 0:
        raise ValueError("Bit length must be non-negative")
    if value < 0:
        raise ValueError("Value cannot be negative for this operation")
    if value.bit_length() > length:
        raise ValueError(f"Value {value} exceeds {length} bits")
    return format(value, f'0{length}b')

if __name__ == '__main__':
    sample_value = 10
    sample_length = 8
    result = to_zero_padded_binary(sample_value, sample_length)
    print(result)
    sample_value_2 = 15
    sample_length_2 = 4
    result_2 = to_zero_padded_binary(sample_value_2, sample_length_2)
    print(result_2)