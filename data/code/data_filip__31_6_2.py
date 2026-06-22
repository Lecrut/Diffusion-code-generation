def hex_to_int(hex_str):
    if not isinstance(hex_str, str):
        raise ValueError("Input must be a string")
    if len(hex_str) == 0:
        raise ValueError("Input string cannot be empty")
    if hex_str.startswith(('0x', '0X')):
        hex_str = hex_str[2:]
    if not all(c in '0123456789abcdefABCDEF' for c in hex_str):
        raise ValueError("Invalid hexadecimal character")
    if len(hex_str) == 0:
        raise ValueError("Input string cannot be empty after stripping prefix")
    return int(hex_str, 16)

if __name__ == '__main__':
    print(hex_to_int("1A"))
    print(hex_to_int("FF"))
    print(hex_to_int("0x10"))
    try:
        hex_to_int("GG")
    except ValueError as e:
        print(f"Caught error: {e}")
    try:
        hex_to_int("")
    except ValueError as e:
        print(f"Caught error: {e}")