import re

def decompress_rle(compressed_string):
    if not compressed_string:
        return ""
    
    pattern = re.compile(r'(\D)(\d+)')
    matches = pattern.findall(compressed_string)
    
    if not matches and re.search(r'\d', compressed_string):
        raise ValueError("Invalid RLE format: Number found without a preceding character.")
    
    if not matches and not re.search(r'\d', compressed_string):
        return compressed_string
    
    result = []
    for char, count in matches:
        result.append(char * int(count))
    
    return "".join(result)

if __name__ == '__main__':
    sample_input = "a5b2c3d1"
    original_string = decompress_rle(sample_input)
    print(original_string)