def binary_to_hex(binary_str: str) -> str:
    cleaned = binary_str.strip()
    if not cleaned:
        raise ValueError("Empty binary string")
    if not all(c in '01' for c in cleaned):
        raise ValueError("Invalid binary characters")
    decimal_value = int(cleaned, 2)
    return hex(decimal_value)[2:].upper()

if __name__ == '__main__':
    samples = [
        "1010",
        "11110000",
        "11011111",
        "1000000000",
        "1"
    ]
    for sample in samples:
        result = binary_to_hex(sample)
        print(result)