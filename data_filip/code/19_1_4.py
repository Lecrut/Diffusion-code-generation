import re

def decode_rle(encoded):
    if not encoded:
        return ""
    pattern = r'(\d+)([a-zA-Z])'
    matches = re.findall(pattern, encoded)
    if not matches:
        raise ValueError("Invalid RLE format")
    decoded = []
    for count, char in matches:
        decoded.append(char * int(count))
    return ''.join(decoded)

if __name__ == '__main__':
    sample1 = "3a12bc2x"
    print(decode_rle(sample1))
    sample2 = "10z5A"
    print(decode_rle(sample2))
    sample3 = "a1b"
    print(decode_rle(sample3))