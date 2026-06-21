def run_length_encode(input_string: str) -> list[tuple[str, int]]:
    if not input_string:
        return []
    
    encoded_list = []
    current_char = input_string[0]
    count = 1
    
    for char in input_string[1:]:
        if char == current_char:
            count += 1
        else:
            encoded_list.append((current_char, count))
            current_char = char
            count = 1
    encoded_list.append((current_char, count))
    
    return encoded_list

if __name__ == '__main__':
    sample_text = "aaabbc"
    result = run_length_encode(sample_text)
    print(result)