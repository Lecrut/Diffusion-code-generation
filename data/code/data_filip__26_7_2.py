def run_length_encode(data: str) -> str:
    if not data:
        return ""
    
    result = []
    count = 1
    current_char = data[0]
    
    for i in range(1, len(data)):
        char = data[i]
        if char == current_char:
            count += 1
        else:
            result.append(str(count))
            result.append(current_char)
            current_char = char
            count = 1
    
    result.append(str(count))
    result.append(current_char)
    
    return "".join(result)

if __name__ == '__main__':
    sample_text = "aaabbbccca"
    encoded_result = run_length_encode(sample_text)
    print(encoded_result)