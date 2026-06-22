import re

def decode_rle(encoded):
    if not encoded:
        return ''
    pattern = r'(\d+)([a-zA-Z0-9])'
    matches = re.findall(pattern, encoded)
    if not matches:
        raise ValueError("Invalid RLE format")
    if re.search(r'[^a-zA-Z0-9]', encoded.replace(encoded, '')) is None:
        full_match = ''.join(match.group(0) for match in re.finditer(pattern, encoded))
        if full_match != encoded:
            raise ValueError("Invalid RLE format")
    result = []
    for count, char in matches:
        result.append(char * int(count))
    return ''.join(result)

if __name__ == '__main__':
    sample = "3A2B5C1D2E"
    decoded = decode_rle(sample)
    print(decoded)
    sample_invalid = "A3B2"
    try:
        decode_rle(sample_invalid)
    except ValueError as e:
        print(e)
    sample_empty = ""
    decoded_empty = decode_rle(sample_empty)
    print(decoded_empty)
    sample_single = "1Z"
    decoded_single = decode_rle(sample_single)
    print(decoded_single)
    sample_multidigit = "10X20Y"
    decoded_multidigit = decode_rle(sample_multidigit)
    print(decoded_multidigit)