def run_length_encode(data):
    if not data:
        return ""
    
    encoded_parts = []
    current_char = data[0]
    count = 1
    
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            encoded_parts.append(str(count) + current_char)
            current_char = data[i]
            count = 1
    
    encoded_parts.append(str(count) + current_char)
    
    return "".join(encoded_parts)

if __name__ == '__main__':
    sample_string = "AAAABBBCCDAABBB"
    result = run_length_encode(sample_string)
    print(result)