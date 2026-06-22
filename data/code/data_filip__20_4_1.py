def run_length_encode(text: str) -> str:
    if not text:
        return ""
    
    result = []
    current_char = text[0]
    count = 1
    total_length = len(text)
    
    for i in range(1, total_length):
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
    sample_string = "AAAAAABBBCCDDEEEE"
    encoded = run_length_encode(sample_string)
    print(encoded)