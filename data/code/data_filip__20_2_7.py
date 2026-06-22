def run_length_encode(binary_sequence: str) -> str:
    if not binary_sequence:
        return ""
    
    result = []
    current_char = binary_sequence[0]
    count = 1
    
    for i in range(1, len(binary_sequence)):
        if binary_sequence[i] == current_char:
            count += 1
        else:
            result.append((count, current_char))
            current_char = binary_sequence[i]
            count = 1
    
    result.append((count, current_char))
    
    output = ""
    for count, char in result:
        if count == 1:
            output += f"{char}"
        else:
            output += f"{count}{char}"
            
    return output

if __name__ == '__main__':
    sample_data = "11000111110011"
    encoded = run_length_encode(sample_data)
    print(encoded)