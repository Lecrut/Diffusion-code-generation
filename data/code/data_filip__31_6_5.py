VALID_HEX_CHARS = frozenset("0123456789abcdefABCDEF")

def parse_hex_to_int(hex_string):
    if not isinstance(hex_string, str):
        raise ValueError("Input must be a string")
    if len(hex_string) == 0:
        raise ValueError("Input string cannot be empty")
    core = hex_string
    if hex_string.startswith("0x") or hex_string.startswith("0X"):
        core = hex_string[2:]
    if len(core) == 0:
        raise ValueError("No hex digits provided")
    for character in core:
        if character not in VALID_HEX_CHARS:
            raise ValueError("Invalid hex character found")
    return int(core, 16)

if __name__ == '__main__':
    result1 = parse_hex_to_int("1A")
    print(result1)
    result2 = parse_hex_to_int("0xFF")
    print(result2)
    result3 = parse_hex_to_int("0")
    print(result3)
    try:
        parse_hex_to_int("G1")
    except ValueError:
        print("ValueError raised for G1")
    try:
        parse_hex_to_int("")
    except ValueError:
        print("ValueError raised for empty string")
    try:
        parse_hex_to_int("0x")
    except ValueError:
        print("ValueError raised for 0x")