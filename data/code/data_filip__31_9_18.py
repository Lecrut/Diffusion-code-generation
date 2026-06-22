def hex_string_to_int(hex_str: str) -> int:
    hex_str = hex_str.strip()
    if hex_str.startswith("0x") or hex_str.startswith("0X"):
        hex_str = hex_str[2:]
    if not hex_str:
        return 0
    result = 0
    for char in hex_str:
        if "0" <= char <= "9":
            digit = ord(char) - 48
        elif "a" <= char <= "f":
            digit = ord(char) - 87
        elif "A" <= char <= "F":
            digit = ord(char) - 55
        else:
            raise ValueError(f"Invalid hexadecimal character: {char}")
        result = (result << 4) | digit
    return result

if __name__ == "__main__":
    sample_values = ["1A3F", "0xFF", "0xdeadbeef", "ABC", "0"]
    for val in sample_values:
        print(hex_string_to_int(val))