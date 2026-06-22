def to_twos_complement_binary(n, bits=8):
    if n >= 0:
        return format(n, f'0{bits}b')
    if n < -(2 ** (bits - 1)) or n >= 2 ** (bits - 1):
        raise ValueError(f"Integer {n} is out of range for {bits}-bit two's complement")
    return format((1 << bits) + n, f'0{bits}b')

if __name__ == '__main__':
    test_values = [-5, -1, 0, 3, -128]
    for value in test_values:
        result = to_twos_complement_binary(value, 8)
        print(f"{value}: {result}")