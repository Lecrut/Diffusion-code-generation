def run_length_encode(data):
    if not data:
        return ""
    
    encoded_result = []
    current_char = data[0]
    count = 1
    
    for i in range(1, len(data)):
        char = data[i]
        if char == current_char:
            count += 1
        else:
            encoded_result.append(str(count))
            encoded_result.append(current_char)
            current_char = char
            count = 1
    
    encoded_result.append(str(count))
    encoded_result.append(current_char)
    
    return "".join(encoded_result)

if __name__ == '__main__':
    sample_input = "aaabbbcccaaa"
    result = run_length_encode(sample_input)
    print(result)