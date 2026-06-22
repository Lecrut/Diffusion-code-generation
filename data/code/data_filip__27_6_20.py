def run_length_encode(input_string: str) -> list[tuple[int, str]]:
    if not input_string:
        return []
    
    encoded_result = []
    current_char = input_string[0]
    count = 1
    
    for i in range(1, len(input_string)):
        char = input_string[i]
        if char == current_char:
            count += 1
        else:
            encoded_result.append((count, current_char))
            current_char = char
            count = 1
    
    encoded_result.append((count, current_char))
    return encoded_result

if __name__ == '__main__':
    sample_string = "AAABBBCCCC"
    result = run_length_encode(sample_string)
    print(result)