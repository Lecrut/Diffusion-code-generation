def run_length_encode(data: str) -> str:
    if not data:
        return ""
    
    if len(data) <= 2:
        return data
    
    result_parts = []
    current_char = data[0]
    current_count = 1
    
    for char in data[1:]:
        if char == current_char:
            current_count += 1
        else:
            result_parts.append(str(current_count))
            result_parts.append(current_char)
            current_char = char
            current_count = 1
    
    result_parts.append(str(current_count))
    result_parts.append(current_char)
    
    return "".join(result_parts)

def run_length_decode(data: str) -> str:
    if not data:
        return ""
    
    result_parts = []
    num_str = []
    
    for char in data:
        if char.isdigit():
            num_str.append(char)
        else:
            count = int("".join(num_str))
            result_parts.append(char * count)
            num_str = []
    
    if num_str:
        count = int("".join(num_str))
        result_parts.append(char * count)
    
    return "".join(result_parts)

if __name__ == '__main__':
    sample_string = "aabcccccaaa"
    encoded = run_length_encode(sample_string)
    print(encoded)
    
    decoded = run_length_decode(encoded)
    print(decoded)