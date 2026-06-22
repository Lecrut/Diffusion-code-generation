from typing import Literal

def hex_to_decimal(hex_input: str) -> int:
    if not isinstance(hex_input, str):
        raise TypeError("Input must be a string")
    hex_input = hex_input.strip().lower()
    if hex_input.startswith("0x"):
        hex_input = hex_input[2:]
    if not hex_input:
        raise ValueError("Input string cannot be empty")
    valid_chars = "0123456789abcdef"
    for char in hex_input:
        if char not in valid_chars:
            raise ValueError(f"Invalid hexadecimal character: {char}")
    total = 0
    power = 0
    for i in range(len(hex_input) - 1, -1, -1):
        char = hex_input[i]
        if char.isdigit():
            value = int(char)
        else:
            value = ord(char) - ord('a') + 10
        total += value * (16 ** power)
        power += 1
    return total

if __name__ == "__main__":
    sample_hex = "1A3F"
    result = hex_to_decimal(sample_hex)
    print(result)
    sample_hex_2 = "0xFF"
    result_2 = hex_to_decimal(sample_hex_2)
    print(result_2)
    sample_hex_3 = "0"
    result_3 = hex_to_decimal(sample_hex_3)
    print(result_3)