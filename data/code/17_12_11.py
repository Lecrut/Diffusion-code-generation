def encode_run_length(text):
    if not text:
        return {}
    
    result = {}
    current_char = None
    count = 0
    
    for char in text:
        if not char.isalnum():
            continue
        if current_char is None:
            current_char = char
            count = 1
        elif char == current_char:
            count += 1
        else:
            if current_char in result:
                result[current_char] += count
            else:
                result[current_char] = count
            current_char = char
            count = 1
    
    if current_char is not None:
        if current_char in result:
            result[current_char] += count
        else:
            result[current_char] = count
            
    return result

if __name__ == '__main__':
    sample_text = "aaabbc"
    encoded_dict = encode_run_length(sample_text)
    print(encoded_dict)