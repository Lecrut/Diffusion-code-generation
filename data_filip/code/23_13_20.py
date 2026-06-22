def run_length_encode(data: str) -> str:
    if not data:
        return ""
    
    encoded_chars = []
    count = 1
    current_char = data[0]
    
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            encoded_chars.append(str(count))
            encoded_chars.append(current_char)
            current_char = data[i]
            count = 1
    
    encoded_chars.append(str(count))
    encoded_chars.append(current_char)
    
    return "".join(encoded_chars)

if __name__ == '__main__':
    test_string = "wwwwaaadexxxxxx"
    result = run_length_encode(test_string)
    print(result)