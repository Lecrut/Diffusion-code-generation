import itertools
import re

def rle_encode(data: str) -> str:
    if not data:
        return ''
    encoded = []
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append(f"{count}{current_char}")
            current_char = char
            count = 1
    encoded.append(f"{count}{current_char}")
    return ''.join(encoded)

def rle_decode(encoded: str) -> str:
    if not encoded:
        return ''
    decoded = []
    pattern = re.compile(r'(\d+)([^\d])')
    for match in pattern.finditer(encoded):
        count = int(match.group(1))
        char = match.group(2)
        decoded.append(char * count)
    return ''.join(decoded)

if __name__ == '__main__':
    test_cases = [
        'AAAABBBCCDAA',
        'ABC',
        'AAAAAAAAAA',
        '',
        'A',
        'AABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQRRSSTTUUVVWWXXYYZZ'
    ]
    
    for test in test_cases:
        encoded = rle_encode(test)
        decoded = rle_decode(encoded)
        print(f"Original: '{test}'")
        print(f"Encoded: '{encoded}'")
        print(f"Decoded: '{decoded}'")
        print(f"Fidelity: {test == decoded}")
        print()