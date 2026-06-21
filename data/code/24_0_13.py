def run_length_encode(input_string: str) -> str:
    if not input_string:
        return ""
    
    encoded = []
    count = 1
    current_char = input_string[0]
    
    for char in input_string[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append(current_char)
            encoded.append(str(count))
            current_char = char
            count = 1
            
    encoded.append(current_char)
    encoded.append(str(count))
    
    return "".join(encoded)

if __name__ == '__main__':
    sample_input = "AAABBBCCCDDDDD"
    result = run_length_encode(sample_input)
    print(result)