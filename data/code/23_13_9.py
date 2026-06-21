def run_length_encode(input_string: str) -> str:
    if not input_string:
        return ""
    
    encoded = []
    count = 1
    prev_char = input_string[0]
    
    for i in range(1, len(input_string)):
        current_char = input_string[i]
        if current_char == prev_char:
            count += 1
        else:
            encoded.append(prev_char)
            if count > 1:
                encoded.append(str(count))
            count = 1
            prev_char = current_char
    
    encoded.append(prev_char)
    if count > 1:
        encoded.append(str(count))
    
    return "".join(encoded)

if __name__ == '__main__':
    test_string = "aabcccccaaa"
    result = run_length_encode(test_string)
    print(result)