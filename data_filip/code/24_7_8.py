def rle_encode(data: str) -> str:
    if not data:
        return ""
    
    encoded_parts = []
    count = 1
    current_char = data[0]
    
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            encoded_parts.append(f"{count}{current_char}")
            current_char = data[i]
            count = 1
    encoded_parts.append(f"{count}{current_char}")
    
    return "".join(encoded_parts)

def rle_decode(data: str) -> str:
    if not data:
        return ""
    
    decoded_parts = []
    i = 0
    n = len(data)
    
    while i < n:
        num_str = ""
        while i < n and data[i].isdigit():
            num_str += data[i]
            i += 1
        
        if not num_str:
            break
        
        if i < n:
            count = int(num_str)
            char = data[i]
            decoded_parts.append(char * count)
            i += 1
        else:
            break
            
    return "".join(decoded_parts)

if __name__ == '__main__':
    sample_string = '0011100'
    
    encoded_result = rle_encode(sample_string)
    print(encoded_result)
    
    decoded_result = rle_decode(encoded_result)
    print(decoded_result)
    
    edge_case_empty = rle_encode("")
    print(edge_case_empty)
    
    edge_case_single = rle_encode("1")
    print(edge_case_single)
    
    decoded_single = rle_decode("11")
    print(decoded_single)