def run_length_encode(sequence: str) -> str:
    if not sequence:
        return ""
    
    result = []
    current_char = sequence[0]
    count = 1
    
    for char in sequence[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1
            
    result.append(f"{count}{current_char}")
    return "".join(result)

if __name__ == "__main__":
    sample_sequence = "aaabbc"
    encoded_result = run_length_encode(sample_sequence)
    print(encoded_result)