import re

def decode_rle(compressed: str) -> str:
    if not compressed:
        return ""
    
    pattern = re.compile(r'(\d+)([^\d])')
    matches = pattern.findall(compressed)
    
    decoded_parts = []
    for count_str, char in matches:
        count = int(count_str)
        decoded_parts.append(char * count)
    
    return "".join(decoded_parts)

if __name__ == '__main__':
    sample_compressed = "12A3B4C"
    result = decode_rle(sample_compressed)
    print(result)
    
    sample_compressed2 = "100Z5Y2X"
    result2 = decode_rle(sample_compressed2)
    print(result2)