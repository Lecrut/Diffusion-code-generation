import re

def encode_rle(data: str) -> str:
    if not data:
        return ""
    
    result = []
    current_char = data[0]
    count = 1
    
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = data[i]
            count = 1
    
    result.append(f"{count}{current_char}")
    return "".join(result)

def decode_rle(encoded_data: str) -> str:
    if not encoded_data:
        return ""
    
    result = []
    pattern = re.compile(r"(\d+)(\D)")
    
    for match in pattern.finditer(encoded_data):
        count = int(match.group(1))
        char = match.group(2)
        result.append(char * count)
    
    return "".join(result)

if __name__ == '__main__':
    original = "AAABBBCCDAA"
    encoded = encode_rle(original)
    print(encoded)
    
    decoded = decode_rle(encoded)
    print(decoded)
    
    empty_encoded = encode_rle("")
    print(empty_encoded)
    
    single_encoded = encode_rle("Z")
    print(single_encoded)
    
    decoded_single = decode_rle("1Z")
    print(decoded_single)