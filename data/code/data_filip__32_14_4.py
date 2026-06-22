def binary_to_hex(input_binary: str) -> str:
    if not input_binary:
        return ""
    
    required_padding = len(input_binary) % 4
    if required_padding:
        input_binary = "0" * (4 - required_padding) + input_binary
    
    hex_chars = []
    for i in range(0, len(input_binary), 4):
        nibble = input_binary[i : i + 4]
        val = int(nibble, 2)
        hex_chars.append(format(val, "X"))
        
    return "".join(hex_chars)

if __name__ == "__main__":
    binary_input = "101100101011"
    print(binary_to_hex(binary_input))