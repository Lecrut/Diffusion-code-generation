def binary_to_hex(binary_str):
    if not binary_str:
        return "0"
    
    valid_chars = set("01")
    for char in binary_str:
        if char not in valid_chars:
            raise ValueError("Input string must contain only 0s and 1s")

    if binary_str.startswith("0") and len(binary_str) > 1:
        binary_str = binary_str.lstrip("0")
        if not binary_str:
            return "0"

    padding_needed = (4 - len(binary_str) % 4) % 4
    binary_str = "0" * padding_needed + binary_str

    hex_digits = "0123456789abcdef"
    hex_result = []

    for i in range(0, len(binary_str), 4):
        chunk = binary_str[i:i+4]
        value = 0
        for bit in chunk:
            value = (value << 1) + int(bit)
        hex_result.append(hex_digits[value])

    result_str = "".join(hex_result)
    result_str = result_str.lstrip("0")
    if not result_str:
        return "0"
    return result_str

if __name__ == '__main__':
    samples = ["1010", "1111", "0", "111111111111", "10101010"]
    for s in samples:
        print(binary_to_hex(s))