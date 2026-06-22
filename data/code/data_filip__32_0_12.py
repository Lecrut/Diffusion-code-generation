def binary_to_hex(binary_str: str) -> str:
    if not binary_str:
        return ""

    remainder = len(binary_str) % 4
    if remainder != 0:
        padded_binary = "0" * (4 - remainder) + binary_str
    else:
        padded_binary = binary_str

    hex_map = {
        "0000": "0",
        "0001": "1",
        "0010": "2",
        "0011": "3",
        "0100": "4",
        "0101": "5",
        "0110": "6",
        "0111": "7",
        "1000": "8",
        "1001": "9",
        "1010": "A",
        "1011": "B",
        "1100": "C",
        "1101": "D",
        "1110": "E",
        "1111": "F"
    }

    hex_result = []
    for i in range(0, len(padded_binary), 4):
        nibble = padded_binary[i:i + 4]
        hex_result.append(hex_map[nibble])

    result = "".join(hex_result)
    if result[0] == "0" and len(result) > 1:
        result = result.lstrip("0")
        if not result:
            result = "0"
    return result

if __name__ == "__main__":
    print(binary_to_hex("0"))
    print(binary_to_hex("1"))
    print(binary_to_hex("1010"))
    print(binary_to_hex("1111"))
    print(binary_to_hex("11011"))
    print(binary_to_hex("11111111"))
    print(binary_to_hex("0000"))
    print(binary_to_hex("10000000"))