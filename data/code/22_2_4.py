import re

def decompress_rle(encoded: str) -> str:
    if not encoded:
        return ''
    pattern = re.compile(r'(\d*)(\D)')
    matches = pattern.findall(encoded)
    decoded_parts = [char * (int(count) if count else 1) for count, char in matches]
    return ''.join(decoded_parts)

if __name__ == '__main__':
    sample_inputs = [
        "a3b4c2d1",
        "abc",
        "a10b5",
        "",
        "z0",
        "1a2b"
    ]
    for inp in sample_inputs:
        result = decompress_rle(inp)
        print(result)