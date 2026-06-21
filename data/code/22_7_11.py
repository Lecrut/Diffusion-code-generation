import re

def rle_decode(compressed: str) -> str:
    if not compressed:
        return ""
    
    def replace_match(match):
        count = int(match.group(1))
        char = match.group(2)
        return char * count
    
    pattern = r'(\d+)(\D)'
    result = re.sub(pattern, replace_match, compressed)
    return result

if __name__ == '__main__':
    compressed_input = "3a4b1c"
    decoded_output = rle_decode(compressed_input)
    print(decoded_output)