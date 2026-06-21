def binary_to_hex(binary_string):
    if not binary_string:
        return "0"

    if len(binary_string) % 4 != 0:
        binary_string = "0" * (4 - len(binary_string) % 4) + binary_string

    hex_map = {
        "0000": "0", "0001": "1", "0010": "2", "0011": "3",
        "0100": "4", "0101": "5", "0110": "6", "0111": "7",
        "1000": "8", "1001": "9", "1010": "A", "1011": "B",
        "1100": "C", "1101": "D", "1110": "E", "1111": "F",
    }

    result = []
    for i in range(0, len(binary_string), 4):
        nibble = binary_string[i : i + 4]
        result.append(hex_map[nibble])

    final_result = "".join(result)
    leading_zeros = 0
    while leading_zeros < len(final_result) - 1 and final_result[leading_zeros] == "0":
        leading_zeros += 1
    return final_result[leading_zeros:]

if __name__ == "__main__":
    print(binary_to_hex("1010"))
    print(binary_to_hex("11111111"))
    print(binary_to_hex("0"))
    print(binary_to_hex("1111000011110000"))