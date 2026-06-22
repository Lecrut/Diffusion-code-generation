def binary_to_hex(binary_string):
    if not binary_string:
        return "0"
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
    length = len(binary_string)
    remainder = length % 4
    if remainder != 0:
        padding = 4 - remainder
        binary_string = "0" * padding + binary_string
    hex_result = ""
    for i in range(0, len(binary_string), 4):
        chunk = binary_string[i : i + 4]
        hex_digit = hex_map.get(chunk)
        if hex_digit is None:
            raise ValueError("Invalid binary string")
        hex_result += hex_digit
    if not hex_result:
        return "0"
    return hex_result

if __name__ == "__main__":
    sample_binary = "11010111010"
    print(binary_to_hex(sample_binary))
    sample_binary_two = "1111"
    print(binary_to_hex(sample_binary_two))