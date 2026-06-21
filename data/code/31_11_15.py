def parse_hex(hex_string):
    if not isinstance(hex_string, str):
        raise TypeError("Input must be a string")
    
    stripped = hex_string.strip()
    
    if stripped.startswith(('0x', '0X')):
        hex_part = stripped[2:]
    else:
        hex_part = stripped
    
    if not hex_part:
        return 0
    
    try:
        result = int(hex_part, 16)
        if stripped.startswith('-'):
            result = -result
        return result
    except ValueError:
        return 0

if __name__ == '__main__':
    samples = [
        "0x1A",
        "0XFF",
        "-0x10",
        "0x0",
        "0x",
        "",
        "GHI",
        "0x123abc",
        "  0xDEAD  "
    ]
    
    for s in samples:
        val = parse_hex(s)
        print(val)