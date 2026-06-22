def encode_rle(data):
    if not data:
        return ""
    
    result = []
    current_char = data[0]
    count = 1
    
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1
    
    result.append(f"{count}{current_char}")
    return "".join(result)

def decode_rle(encoded_data):
    decoded = []
    i = 0
    while i < len(encoded_data):
        count = 0
        while i < len(encoded_data) and encoded_data[i].isdigit():
            count = count * 10 + int(encoded_data[i])
            i += 1
        
        if i < len(encoded_data):
            char = encoded_data[i]
            i += 1
            decoded.append(char * count)
    
    return "".join(decoded)

if __name__ == '__main__':
    sample_string = "AAAABBBCCDAA"
    encoded = encode_rle(sample_string)
    print(encoded)
    
    decoded = decode_rle(encoded)
    print(decoded)
    
    another_sample = "Hello World"
    encoded_another = encode_rle(another_sample)
    print(encoded_another)
    
    decoded_another = decode_rle(encoded_another)
    print(decoded_another)