def run_length_encode(sequence: str) -> str:
    if not sequence:
        return ""
    
    result = []
    current_char = sequence[0]
    count = 1
    
    for i in range(1, len(sequence)):
        char = sequence[i]
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1
    
    result.append(f"{count}{current_char}")
    return "".join(result)

if __name__ == '__main__':
    sequence = "112223333"
    encoded = run_length_encode(sequence)
    print(encoded)