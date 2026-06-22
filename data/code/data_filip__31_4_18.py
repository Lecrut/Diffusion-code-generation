import builtins

def hex_strings_to_integers(hex_strings):
    result = []
    for hex_string in hex_strings:
        stripped = hex_string.strip()
        if stripped.startswith("0x") or stripped.startswith("0X"):
            stripped = stripped[2:]
        value = int(stripped, 16)
        result.append(value)
    return result

if __name__ == '__main__':
    sample_data = ["0x1A", "FF", "0X10", "cafe"]
    output = hex_strings_to_integers(sample_data)
    print(output)