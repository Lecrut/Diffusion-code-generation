def binary_to_hex(binary_string):
    if not binary_string:
        return ""
    
    padding_length = 4 - len(binary_string) % 4
    if padding_length < 4:
        padded = "0" * padding_length + binary_string
    else:
        padded = binary_string
    
    hex_mapping = {
        "0000": "0", "0001": "1", "0010": "2", "0011": "3",
        "0100": "4", "0101": "5", "0110": "6", "0111": "7",
        "1000": "8", "1001": "9", "1010": "A", "1011": "B",
        "1100": "C", "1101": "D", "1110": "E", "1111": "F"
    }
    
    result = []
    for i in range(0, len(padded), 4):
        segment = padded[i:i + 4]
        result.append(hex_mapping[segment])
    
    return "".join(result)

if __name__ == '__main__':
    binary_data = "101011001111"
    hex_result = binary_to_hex(binary_data)
    print(hex_result)