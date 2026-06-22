def run_length_encode(data):
    if not data:
        return ""
    
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
    return "".join(encoded)

def run_length_decode(encoded_data):
    if not encoded_data:
        return ""
    
    decoded = []
    i = 0
    
    while i < len(encoded_data):
        count_str = ""
        while i < len(encoded_data) and encoded_data[i].isdigit():
            count_str += encoded_data[i]
            i += 1
        
        count = int(count_str)
        char = encoded_data[i]
        decoded.append(char * count)
        i += 1
    
    return "".join(decoded)

if __name__ == "__main__":
    sample_string = "AAAABBBCCDAAA"
    encoded_result = run_length_encode(sample_string)
    print(f"Encoded: {encoded_result}")
    
    decoded_result = run_length_decode(encoded_result)
    print(f"Decoded: {decoded_result}")