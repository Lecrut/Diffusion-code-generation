def run_length_encode(data: str) -> str:
    if not data:
        return ""
    
    encoded = []
    current_char = data[0]
    count = 1
    length = len(data)
    
    i = 1
    while i < length:
        char = data[i]
        if char == current_char:
            count += 1
        else:
            encoded.append(f"{count}{current_char}")
            current_char = char
            count = 1
        i += 1
    
    encoded.append(f"{count}{current_char}")
    
    return "".join(encoded)

if __name__ == '__main__':
    sample_string = "AAABBBCCCDDDD"
    result = run_length_encode(sample_string)
    print(result)