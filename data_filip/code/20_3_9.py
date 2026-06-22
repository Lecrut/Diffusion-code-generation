def run_length_encode(input_str):
    if not input_str:
        return ""
    
    encoded = []
    count = 1
    current_char = input_str[0]
    
    for i in range(1, len(input_str)):
        if input_str[i] == current_char:
            count += 1
        else:
            encoded.append(str(count) + current_char)
            current_char = input_str[i]
            count = 1
    
    encoded.append(str(count) + current_char)
    
    return "".join(encoded)

if __name__ == '__main__':
    text = "aaabbc"
    result = run_length_encode(text)
    print(result)