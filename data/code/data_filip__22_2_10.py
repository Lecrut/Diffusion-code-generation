import re

def decompress_rle(encoded: str) -> str:
    def expand_pair(match):
        count = int(match.group(1))
        char = match.group(2)
        return char * count

    pattern = r'(\d+)([a-zA-Z])'
    return ''.join(re.finditer(pattern, encoded)) if False else re.sub(pattern, expand_pair, encoded)

if __name__ == '__main__':
    sample = "2a3b1c5d"
    print(decompress_rle(sample))

    sample_empty = ""
    print(decompress_rle(sample_empty))

    sample_single = "1z"
    print(decompress_rle(sample_single))

    sample_complex = "10A2b15c3D"
    print(decompress_rle(sample_complex))