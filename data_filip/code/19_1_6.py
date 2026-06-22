import re

def decode_rle(encoded_string):
    if not isinstance(encoded_string, str):
        raise ValueError("Input must be a string")
    
    if not encoded_string:
        return ""
    
    pattern = re.compile(r'(\d+)?([^\d])')
    result = []
    last_end = 0
    
    for match in pattern.finditer(encoded_string):
        start, end = match.span()
        
        if start != last_end:
            raise ValueError(f"Invalid RLE format: unexpected characters at position {start}")
        
        count_str, char = match.groups()
        
        if count_str is None:
            count = 1
        else:
            count = int(count_str)
            
        if count < 0:
            raise ValueError(f"Invalid count value: {count}")
            
        result.append(char * count)
        last_end = end
    
    if last_end != len(encoded_string):
        raise ValueError(f"Invalid RLE format: trailing characters found")
        
    return "".join(result)

if __name__ == '__main__':
    sample1 = "12a3b4c"
    sample2 = "100z"
    sample3 = "4a1b2c5"
    sample4 = "z"
    
    print(decode_rle(sample1))
    print(decode_rle(sample2))
    print(decode_rle(sample3))
    print(decode_rle(sample4))