def binary_to_hex(binary_input: str) -> str:
    binary_input = binary_input.strip()
    if not binary_input:
        return ""
    if any(char not in '01' for char in binary_input):
        raise ValueError("Input must be a binary string")
    decimal_value = int(binary_input, 2)
    hex_value = hex(decimal_value)[2:].upper()
    padding_needed = (4 - len(hex_value) % 4) % 4
    hex_value = hex_value.zfill(padding_needed + len(hex_value))
    return hex_value

if __name__ == '__main__':
    sample_inputs = [
        "1010",
        "11110000",
        "11011111",
        "0",
        "1",
        "1111111111111111"
    ]
    for sample in sample_inputs:
        result = binary_to_hex(sample)
        print(result)