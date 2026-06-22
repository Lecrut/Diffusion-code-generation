def convert_binaries_to_hex(binaries: list[str]) -> list[str]:
    results = []
    for b in binaries:
        if not b:
            raise ValueError("Empty binary string")
        if not all(c in '01' for c in b):
            raise ValueError(f"Invalid binary string: {b}")
        decimal_val = int(b, 2)
        hex_str = hex(decimal_val)[2:].upper()
        results.append(hex_str)
    return results

if __name__ == '__main__':
    samples = ["0", "1", "1010", "1111", "10000000", "1111111111111111"]
    result = convert_binaries_to_hex(samples)
    print(result)