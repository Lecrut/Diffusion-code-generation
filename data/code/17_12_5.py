def encode_run_length(text):
    if not text:
        return {}
    
    result = {}
    count = 1
    current_char = text[0]
    
    for i in range(1, len(text)):
        char = text[i]
        if char == current_char:
            count += 1
        else:
            if current_char.isalnum():
                if current_char in result:
                    result[current_char] += count
                else:
                    result[current_char] = count
            current_char = char
            count = 1
    
    if current_char.isalnum():
        if current_char in result:
            result[current_char] += count
        else:
            result[current_char] = count
            
    return result

if __name__ == '__main__':
    sample_input = "AAABBBCCDAA"
    encoded_output = encode_run_length(sample_input)
    print(encoded_output)