import re

def decode_rle(rle_string):
    if not rle_string:
        return ""
    pattern = r'(\d+)([A-Za-z])'
    matches = re.findall(pattern, rle_string)
    result = []
    for count, char in matches:
        result.append(char * int(count))
    return ''.join(result)

if __name__ == '__main__':
    sample_inputs = [
        "12W3B2A5Z",
        "10H5K",
        "1A1B1C",
        "99Z1a",
        "",
        "A3B",
        "0X"
    ]
    for sample in sample_inputs:
        decoded = decode_rle(sample)
        print(f"Input: '{sample}' -> Output: '{decoded}'")