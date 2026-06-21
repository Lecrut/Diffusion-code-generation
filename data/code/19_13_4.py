def run_length_encode(sequence: str) -> str:
    if not sequence:
        return ""
    
    encoded_chars = []
    count = 1
    current_char = sequence[0]
    
    for char in sequence[1:]:
        if char == current_char:
            count += 1
        else:
            encoded_chars.append(f"{count}{current_char}")
            current_char = char
            count = 1
    
    encoded_chars.append(f"{count}{current_char}")
    
    return "".join(encoded_chars)

if __name__ == "__main__":
    sequence = "aaabbbccccc"
    result = run_length_encode(sequence)
    print(result)