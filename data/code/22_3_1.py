import re

def rle_encode(data):
    if not data:
        return ''
    
    encoded = []
    current_char = data[0]
    count = 1
    
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append(f"{count}{current_char}")
            current_char = char
            count = 1
    
    encoded.append(f"{count}{current_char}")
    return ''.join(encoded)

def rle_decode(data):
    if not data:
        return ''
    
    decoded = []
    pattern = re.compile(r'(\d+)(\D)')
    
    for match in pattern.finditer(data):
        count = int(match.group(1))
        char = match.group(2)
        decoded.append(char * count)
    
    return ''.join(decoded)

if __name__ == '__main__':
    sample_string = 'AAAABBBCCDAA'
    encoded = rle_encode(sample_string)
    print(encoded)
    decoded = rle_decode(encoded)
    print(decoded)