def run_length_encode(data: str, max_run_length: int = 9) -> str:
    if not data:
        return ""
    
    if not isinstance(max_run_length, int) or max_run_length < 1:
        raise ValueError("max_run_length must be a positive integer")
    
    encoded_parts = []
    current_char = data[0]
    current_count = 1
    
    for i in range(1, len(data)):
        char = data[i]
        if char == current_char:
            if current_count < max_run_length:
                current_count += 1
            else:
                encoded_parts.append(f"{current_count}{current_char}")
                current_count = 1
        else:
            encoded_parts.append(f"{current_count}{current_char}")
            current_char = char
            current_count = 1
            
    encoded_parts.append(f"{current_count}{current_char}")
    
    return "".join(encoded_parts)

if __name__ == '__main__':
    result = run_length_encode("AAAAABBBCCDEEE", 3)
    print(result)