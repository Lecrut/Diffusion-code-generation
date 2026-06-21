def binary_to_hex(binary_input: str) -> str:
    if not isinstance(binary_input, str):
        raise TypeError("Input must be a string")
    binary_input = binary_input.strip()
    if not binary_input:
        return "0"
    if not all(c in '01' for c in binary_input):
        raise ValueError("Input must contain only binary digits (0 and 1)")
    decimal_value = int(binary_input, 2)
    hex_value = hex(decimal_value)[2:].upper()
    return hex_value

if __name__ == '__main__':
    samples = ["0", "1", "1010", "11110000", "101010101010", "111111111111"]
    results = [binary_to_hex(s) for s in samples]
    print(results)