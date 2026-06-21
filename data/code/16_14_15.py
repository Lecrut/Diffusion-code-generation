def run_length_encode(data: str) -> str:
    if not data:
        return ""
    
    encoded_chars = []
    current_char = data[0]
    count = 1
    
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            encoded_chars.append(current_char + str(count))
            current_char = char
            count = 1
    
    encoded_chars.append(current_char + str(count))
    
    return "".join(encoded_chars)

if __name__ == "__main__":
    sample_input = "AAABBBCCCCCCCCCCDDEEEEF"
    result = run_length_encode(sample_input)
    print(result)
    empty_input = ""
    print(run_length_encode(empty_input))
    single_char_input = "A"
    print(run_length_encode(single_char_input))
    mixed_input = "AABBAA"
    print(run_length_encode(mixed_input))