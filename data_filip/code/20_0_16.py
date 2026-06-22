def run_length_encode(data: str) -> str:
    if not data:
        return ""
    
    encoded = []
    current_char = data[0]
    count = 1
    length = len(data)
    
    for i in range(1, length):
        char = data[i]
        if char == current_char:
            count += 1
        else:
            encoded.append(str(count) + current_char)
            current_char = char
            count = 1
    encoded.append(str(count) + current_char)
    
    return "".join(encoded)

if __name__ == "__main__":
    sample_input = "aabcccccaaa"
    result = run_length_encode(sample_input)
    print(result)