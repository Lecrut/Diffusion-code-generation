import re

def decode_rle(rle_string):
    if not isinstance(rle_string, str):
        raise ValueError("Input must be a string")
    
    if not rle_string:
        return ""
    
    pattern = re.compile(r'(\d+)([a-zA-Z])|([a-zA-Z])')
    result = []
    pos = 0
    
    while pos < len(rle_string):
        match = pattern.match(rle_string[pos:])
        if not match:
            raise ValueError(f"Invalid RLE encoding at position {pos}: '{rle_string[pos:]}'")
        
        if match.group(2):
            count = int(match.group(1))
            char = match.group(2)
            result.append(char * count)
            pos += len(match.group(1)) + 1
        elif match.group(3):
            char = match.group(3)
            result.append(char)
            pos += 1
        else:
            raise ValueError(f"Invalid RLE encoding at position {pos}")
    
    return ''.join(result)

if __name__ == '__main__':
    sample1 = "3A2B5C"
    sample2 = "12X1Y"
    sample3 = "A"
    sample4 = "2a3B4c"
    sample5 = ""
    
    print(decode_rle(sample1))
    print(decode_rle(sample2))
    print(decode_rle(sample3))
    print(decode_rle(sample4))
    print(decode_rle(sample5))