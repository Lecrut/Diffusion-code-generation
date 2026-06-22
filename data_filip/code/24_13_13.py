import re

def rle_encode(data):
    if not data:
        return ""
    
    encoded_parts = []
    current_char = data[0]
    count = 1
    
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            encoded_parts.append(f"{current_char}{count}")
            current_char = char
            count = 1
            
    encoded_parts.append(f"{current_char}{count}")
    
    return "".join(encoded_parts)

def rle_decode(encoded_data):
    if not encoded_data:
        return ""
    
    decoded_parts = []
    pattern = re.compile(r'([a-zA-Z])(\d+)')
    matches = pattern.findall(encoded_data)
    
    for char, count_str in matches:
        count = int(count_str)
        decoded_parts.append(char * count)
        
    return "".join(decoded_parts)

if __name__ == '__main__':
    sample_data = "AAAABBBCCDAA"
    encoded = rle_encode(sample_data)
    decoded = rle_decode(encoded)
    print(f"Original: {sample_data}")
    print(f"Encoded: {encoded}")
    print(f"Decoded: {decoded}")
    
    sample_empty = ""
    print(f"Empty Encoded: {rle_encode(sample_empty)}")
    print(f"Empty Decoded: {rle_decode('')}")
    
    sample_single = "A"
    encoded_single = rle_encode(sample_single)
    decoded_single = rle_decode(encoded_single)
    print(f"Single Char Original: {sample_single}")
    print(f"Single Char Encoded: {encoded_single}")
    print(f"Single Char Decoded: {decoded_single}")