def to_twos_complement(n, bits=8):
    if n == 0:
        return "0" * bits
    if n < 0:
        masked_val = (1 << bits) + n
        return bin(masked_val)[2:].zfill(bits)
    if n >= (1 << bits):
        raise ValueError(f"Value {n} exceeds {bits}-bit representation range")
    return bin(n)[2:].zfill(bits)

if __name__ == "__main__":
    test_values = [-5, -1, 0, 1, 127, -128, -200]
    for value in test_values:
        try:
            result = to_twos_complement(value, bits=8)
            print(f"{value}: {result}")
        except ValueError as e:
            print(f"{value}: Error - {e}")

    for value in [-5, 5]:
        result_16 = to_twos_complement(value, bits=16)
        print(f"{value} (16-bit): {result_16}")