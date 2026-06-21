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
            if count >= 3:
                result.append(str(count))
                result.append(current_char)
            else:
                result.append(current_char)
                result.append(str(count))
            current_char = char
            count = 1
    
    if count >= 3:
        result.append(str(count))
        result.append(current_char)
    else:
        result.append(current_char)
        result.append(str(count))
    
    return "".join(result)

if __name__ == '__main__':
    sample_input = "AAABBBC"
    encoded_output = run_length_encode(sample_input)
    print(encoded_output)