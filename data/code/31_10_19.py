import binascii

def hex_to_int(hex_string: str) -> int:
    cleaned = hex_string.strip()
    if cleaned.startswith(("0x", "0X")):
        cleaned = cleaned[2:]
    if not cleaned:
        return 0
    if not all(c in "0123456789abcdefABCDEF" for c in cleaned):
        raise ValueError("Invalid hexadecimal string")
    return int(cleaned, 16)

if __name__ == "__main__":
    sample_input = "1A3F"
    result = hex_to_int(sample_input)
    print(result)
    sample_input_with_prefix = "0xDEADBEEF"
    result_with_prefix = hex_to_int(sample_input_with_prefix)
    print(result_with_prefix)