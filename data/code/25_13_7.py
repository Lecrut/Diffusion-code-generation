def run_length_encode(data: str) -> str:
    if not data:
        return ""
    
    encoded_parts = []
    current_char = data[0]
    count = 1
    length = len(data)
    
    for i in range(1, length):
        char = data[i]
        if char == current_char:
            count += 1
        else:
            encoded_parts.append(current_char + str(count))
            current_char = char
            count = 1
    
    encoded_parts.append(current_char + str(count))
    
    return "".join(encoded_parts)

def run_length_decode(encoded_data: str) -> str:
    if not encoded_data:
        return ""
    
    decoded_parts = []
    i = 0
    length = len(encoded_data)
    
    while i < length:
        char = encoded_data[i]
        i += 1
        num_str = []
        
        while i < length and encoded_data[i].isdigit():
            num_str.append(encoded_data[i])
            i += 1
        
        count = int("".join(num_str))
        decoded_parts.append(char * count)
    
    return "".join(decoded_parts)

if __name__ == "__main__":
    sample_input = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
    encoded_result = run_length_encode(sample_input)
    print(encoded_result)
    decoded_result = run_length_decode(encoded_result)
    print(decoded_result)