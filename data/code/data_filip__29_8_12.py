def encode_consecutive(text: str) -> str:
    if not text:
        return ""
    
    result = []
    count = 1
    current_char = text[0]
    
    for i in range(1, len(text)):
        char = text[i]
        if char == current_char:
            count += 1
        else:
            result.append(current_char + str(count))
            current_char = char
            count = 1
    
    result.append(current_char + str(count))
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbbcccd"
    encoded_output = encode_consecutive(sample_input)
    print(encoded_output)