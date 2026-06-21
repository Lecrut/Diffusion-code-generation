def run_length_encode(text: str) -> str:
    if not text:
        return ""
    
    result = []
    count = 1
    length = len(text)
    current_char = text[0]
    
    for i in range(1, length):
        char = text[i]
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1
    
    result.append(f"{count}{current_char}")
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbbccddddd"
    compressed_output = run_length_encode(sample_input)
    print(compressed_output)