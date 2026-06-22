def run_length_encode(input_string: str) -> str:
    if not input_string:
        return ""
    
    encoded = []
    count = 1
    current_char = input_string[0]
    
    for i in range(1, len(input_string)):
        char = input_string[i]
        if char == current_char:
            count += 1
        else:
            encoded.append(f"{count}{current_char}")
            current_char = char
            count = 1
    encoded.append(f"{count}{current_char}")
    
    return "".join(encoded)

if __name__ == "__main__":
    sample_text = "AAABBBCCDAA"
    compressed_result = run_length_encode(sample_text)
    print(compressed_result)