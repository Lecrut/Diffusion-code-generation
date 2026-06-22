import re
from functools import lru_cache

BINARY_PATTERN = re.compile(r'^[01]+$')
HEX_MAP = {
    '0000': '0',
    '0001': '1',
    '0010': '2',
    '0011': '3',
    '0100': '4',
    '0101': '5',
    '0110': '6',
    '0111': '7',
    '1000': '8',
    '1001': '9',
    '1010': 'A',
    '1011': 'B',
    '1100': 'C',
    '1101': 'D',
    '1110': 'E',
    '1111': 'F'
}

def normalize_binary_input(raw_binary: str) -> str:
    cleaned = raw_binary.strip().replace('0b', '').replace(' ', '')
    if not cleaned:
        return '0'
    return cleaned

def validate_binary_string(binary_str: str) -> bool:
    return bool(BINARY_PATTERN.match(binary_str))

@lru_cache(maxsize=128)
def binary_chunk_to_hex(chunk: str) -> str:
    return HEX_MAP[chunk]

def binary_to_hexadecimal(binary_input: str) -> str:
    normalized = normalize_binary_input(binary_input)
    if normalized == '0':
        return '0'
    if not validate_binary_string(normalized):
        raise ValueError('Invalid binary input')
    padded_length = (len(normalized) + 3) // 4 * 4
    padded_binary = normalized.zfill(padded_length)
    chunks = [padded_binary[i:i+4] for i in range(0, len(padded_binary), 4)]
    hex_chars = [binary_chunk_to_hex(chunk) for chunk in chunks]
    return ''.join(hex_chars).lstrip('0') or '0'

if __name__ == '__main__':
    test_cases = ['1010', '11110000', '0', '1', '1111111111111111', '1010101010101010', '11011']
    for case in test_cases:
        print(binary_to_hexadecimal(case))