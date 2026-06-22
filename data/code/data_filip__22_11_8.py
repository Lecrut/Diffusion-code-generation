import re

def decompress_rle(encoded_str):
    if not encoded_str:
        return ""
    
    pattern = re.compile(r'([a-zA-Z])(\d+)')
    matches = pattern.finditer(encoded_str)
    
    result_parts = []
    for match in matches:
        char = match.group(1)
        count = int(match.group(2))
        result_parts.append(char * count)
    
    return "".join(result_parts)

if __name__ == '__main__':
    sample1 = "a3b2c1"
    sample2 = "Z15y2"
    sample3 = ""
    sample4 = "A1B1C1"
    
    print(decompress_rle(sample1))
    print(decompress_rle(sample2))
    print(decompress_rle(sample3))
    print(decompress_rle(sample4))