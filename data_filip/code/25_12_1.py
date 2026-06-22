import sys

def encode_rle(data):
    if not data:
        return ""
    
    encoded = []
    count = 1
    current_char = data[0]
    
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            encoded.append(str(count) + current_char)
            current_char = data[i]
            count = 1
    
    encoded.append(str(count) + current_char)
    return "".join(encoded)

def decode_rle(data):
    if not data:
        return ""
    
    decoded = []
    count_str = ""
    
    for char in data:
        if char.isdigit():
            count_str += char
        else:
            count = int(count_str)
            decoded.append(char * count)
            count_str = ""
    
    return "".join(decoded)

if __name__ == "__main__":
    sample_text = "AAABBBCCCCDD"
    encoded_result = encode_rle(sample_text)
    print(encoded_result)
    decoded_result = decode_rle(encoded_result)
    print(decoded_result)