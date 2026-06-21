def binary_to_hex(binary_string: str) -> str:
    if not binary_string:
        return "0"
    if len(binary_string) % 4 != 0:
        binary_string = binary_string.zfill(len(binary_string) + (4 - len(binary_string) % 4))
    hex_chars = "0123456789abcdef"
    hex_result = ""
    for i in range(0, len(binary_string), 4):
        nibble = binary_string[i:i + 4]
        value = 0
        for bit in nibble:
            value = value * 2 + (1 if bit == '1' else 0)
        hex_result += hex_chars[value]
    return hex_result.lstrip("0") or "0"

if __name__ == "__main__":
    sample_binaries = ["1010", "11110000", "11011111", "0", "1", "10010101"]
    for binary in sample_binaries:
        result = binary_to_hex(binary)
        print(f"{binary} -> {result}")