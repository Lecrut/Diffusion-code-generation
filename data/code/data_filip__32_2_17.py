_BINARY_TO_HEX_MAP = {
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
    "1111": "F",
}

def _validate_and_pad_binary(binary_str):
    if not binary_str:
        raise ValueError("Input string cannot be empty")
    allowed = frozenset('01')
    if not all(c in allowed for c in binary_str):
        raise ValueError("Input must contain only binary digits (0 and 1)")
    padded_len = len(binary_str) + (4 - len(binary_str) % 4) % 4
    return binary_str.zfill(padded_len)

def _convert_chunk_to_hex(chunk):
    return _BINARY_TO_HEX_MAP[chunk]

def binary_to_hex(binary_str):
    validated_str = _validate_and_pad_binary(binary_str)
    hex_digits = []
    for i in range(0, len(validated_str), 4):
        chunk = validated_str[i:i+4]
        hex_digits.append(_convert_chunk_to_hex(chunk))
    result = ''.join(hex_digits)
    return result.lstrip('0') or "0"

if __name__ == '__main__':
    sample_inputs = [
        "111100001010",
        "1010101010101010",
        "1",
        "1111",
        "0000",
        "10101010",
    ]
    for s in sample_inputs:
        print(binary_to_hex(s))