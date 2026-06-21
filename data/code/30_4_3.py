def to_zero_padded_binary(length, value):
    if length < 1:
        raise ValueError("Length must be at least 1")
    if value < 0 or value >= (1 << length):
        raise ValueError(f"Value {value} does not fit in {length} bits")
    return format(value, f'0{length}b')

if __name__ == '__main__':
    print(to_zero_padded_binary(8, 5))
    print(to_zero_padded_binary(5, 31))
    print(to_zero_padded_binary(16, 256))