def run_length_encode(data: str) -> str:
    if not data:
        return ""
    
    result = []
    current_char = data[0]
    count = 1
    length = len(data)
    
    for i in range(1, length):
        char = data[i]
        if char == current_char:
            count += 1
        else:
            result.append(current_char)
            if count > 1:
                result.append(str(count))
            current_char = char
            count = 1
    
    result.append(current_char)
    if count > 1:
        result.append(str(count))
        
    return "".join(result)

if __name__ == '__main__':
    sample_data = "AAABBBCCCAADDDDD"
    encoded_output = run_length_encode(sample_data)
    print(encoded_output)