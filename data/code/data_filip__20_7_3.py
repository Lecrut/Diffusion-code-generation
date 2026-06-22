def run_length_encode(sequence: str) -> str:
    if not sequence:
        return ""
    
    result = []
    count = 1
    current_char = sequence[0]
    
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
    hard_coded_sequence = "1112223344444"
    encoded_result = run_length_encode(hard_coded_sequence)
    print(encoded_result)