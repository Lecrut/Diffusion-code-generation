def decimal_to_zero_padded_binary(n: int, width: int) -> str:
    if n < 0:
        raise ValueError("Negative numbers are not supported for this format")
    if width <= 0:
        raise ValueError("Width must be a positive integer")
    if n >= (1 << width):
        raise ValueError(f"Value {n} exceeds capacity for {width} bits")
    return format(n, f'0{width}b')

if __name__ == '__main__':
    sample_values = [
        (0, 8),
        (5, 8),
        (15, 4),
        (255, 8),
        (1024, 12)
    ]
    for value, bit_length in sample_values:
        result = decimal_to_zero_padded_binary(value, bit_length)
        print(result)