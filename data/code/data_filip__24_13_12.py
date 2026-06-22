import re

def encode_rle(data: str) -> str:
    if not data:
        return ""
    
    result = []
    count = 1
    current_char = data[0]
    
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = data[i]
            count = 1
    
    result.append(f"{count}{current_char}")
    return "".join(result)

def decode_rle(data: str) -> str:
    if not data:
        return ""
    
    result = []
    pattern = re.compile(r"(\d+)(.)")
    
    for match in pattern.finditer(data):
        count_str, char = match.groups()
        count = int(count_str)
        result.append(char * count)
        
    return "".join(result)

if __name__ == '__main__':
    sample_string = "aaabbbcc"
    encoded = encode_rle(sample_string)
    print(encode_rle(sample_string))
    
    decoded = decode_rle(encoded)
    print(decode_rle(encoded))