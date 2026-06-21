def binary_to_hex(binary_string: str) -> str:
    cleaned = binary_string.replace(' ', '').replace('0b', '').replace('0B', '')
    if not cleaned:
        raise ValueError("Binary string cannot be empty")
    if not all(c in '01' for c in cleaned):
        raise ValueError("Invalid binary string: contains non-binary characters")
    decimal_value = int(cleaned, 2)
    return format(decimal_value, 'X')

if __name__ == '__main__':
    samples = ["1010", "1111", "00001010", "10011101011"]
    for value in samples:
        result = binary_to_hex(value)
        print(f"{value} -> {result}")