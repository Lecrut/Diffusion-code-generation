BINARY_TO_HEX = {
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

def binary_to_hex(binary_str):
    if not binary_str:
        return ""
    if binary_str[0] == "-":
        negative = True
        binary_str = binary_str[1:]
    else:
        negative = False
    if len(binary_str) % 4 != 0:
        binary_str = binary_str.zfill(len(binary_str) + (4 - len(binary_str) % 4))
    hex_result = ""
    for i in range(0, len(binary_str), 4):
        nibble = binary_str[i:i+4]
        hex_result += BINARY_TO_HEX[nibble]
    if negative and hex_result:
        hex_result = "-" + hex_result
    return hex_result

if __name__ == '__main__':
    print(binary_to_hex("1010"))
    print(binary_to_hex("11110000"))
    print(binary_to_hex("0"))
    print(binary_to_hex("11111111"))