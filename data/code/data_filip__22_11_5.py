import re

def decompress_rle(encoded_string):
    if not encoded_string:
        return ""
    pattern = r'(\D)(\d+)'
    matches = re.findall(pattern, encoded_string)
    if not matches:
        raise ValueError("Invalid Run-Length Encoding format")
    result_parts = []
    for char, count in matches:
        result_parts.append(char * int(count))
    return "".join(result_parts)

if __name__ == '__main__':
    sample_encoded = "a3b2c4"
    uncompressed = decompress_rle(sample_encoded)
    print(uncompressed)
    sample_encoded_2 = "x10y1z3"
    uncompressed_2 = decompress_rle(sample_encoded_2)
    print(uncompressed_2)