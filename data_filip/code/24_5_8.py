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

def run_length_decode(data):
    if not data:
        return ""
    
    decoded = []
    i = 0
    
    while i < len(data):
        num_str = ""
        while i < len(data) and data[i].isdigit():
            num_str += data[i]
            i += 1
        
        if i < len(data):
            count = int(num_str)
            char = data[i]
            decoded.append(char * count)
            i += 1
    
    return "".join(decoded)

if __name__ == "__main__":
    test_input = "AAABBBCCCC"
    encoded_result = run_length_encode(test_input)
    print(encoded_result)
    
    decoded_result = run_length_decode(encoded_result)
    print(decoded_result)
    
    mixed_input = "A2B3C4"
    mixed_decoded = run_length_decode(mixed_input)
    print(mixed_decoded)
    
    empty_input = ""
    print(run_length_encode(empty_input))
    print(run_length_decode(empty_input))