import re

def decode_rle(rle_string):
    if not rle_string:
        return ""

    pattern = re.compile(r'(\d+)([A-Za-z])')
    matches = pattern.findall(rle_string)

    if not matches:
        return ""

    decoded_parts = []
    for count_str, char in matches:
        count = int(count_str)
        decoded_parts.append(char * count)

    return ''.join(decoded_parts)

if __name__ == '__main__':
    sample1 = "3A5B2C"
    print(decode_rle(sample1))

    sample2 = "10X"
    print(decode_rle(sample2))

    sample3 = "1a2b3c"
    print(decode_rle(sample3))

    sample4 = ""
    print(decode_rle(sample4))

    sample5 = "100Z1Y"
    print(decode_rle(sample5))