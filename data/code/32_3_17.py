BINARY_HEX_MAP = {
    "0": "0", "1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7",
    "8": "8", "9": "9", "10": "A", "11": "B", "12": "C", "13": "D", "14": "E", "15": "F"
}

def binary_to_hex(binary_string):
    if not binary_string:
        return "0"
    binary_string = binary_string.replace(" ", "").replace("\t", "")
    if not all(c in "01" for c in binary_string):
        raise ValueError("Invalid binary string")
    result = ""
    padding = (4 - len(binary_string) % 4) % 4
    binary_string = "0" * padding + binary_string
    for i in range(0, len(binary_string), 4):
        nibble = binary_string[i:i+4]
        decimal_value = int(nibble, 2)
        hex_char = BINARY_HEX_MAP[str(decimal_value)]
        result += hex_char
    return result.lstrip("0") or "0"

if __name__ == '__main__':
    sample_binaries = ["1010", "11110000", "0", "1"]
    for b in sample_binaries:
        print(f"{b} -> {binary_to_hex(b)}")