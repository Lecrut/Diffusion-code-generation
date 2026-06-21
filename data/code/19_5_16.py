def rle_encode_with_limit(input_string, max_run_length):
    if not input_string:
        return ""
    
    if max_run_length < 1:
        raise ValueError("max_run_length must be at least 1")
    
    encoded_chars = []
    current_char = input_string[0]
    current_count = 1
    
    for i in range(1, len(input_string)):
        char = input_string[i]
        if char == current_char:
            if current_count == max_run_length:
                encoded_chars.append(str(current_count))
                encoded_chars.append(current_char)
                current_count = 1
            else:
                current_count += 1
        else:
            encoded_chars.append(str(current_count))
            encoded_chars.append(current_char)
            current_char = char
            current_count = 1
            
    encoded_chars.append(str(current_count))
    encoded_chars.append(current_char)
    
    return "".join(encoded_chars)

if __name__ == '__main__':
    data = "AAAAAAAAAAA"
    limit = 5
    result = rle_encode_with_limit(data, limit)
    print(result)