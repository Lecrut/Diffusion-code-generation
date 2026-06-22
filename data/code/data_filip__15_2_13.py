def compress_sequence(sequence: str) -> str:
    if not sequence:
        return ""
    
    result = []
    current_char = sequence[0]
    count = 1
    
    for i in range(1, len(sequence)):
        if sequence[i] == current_char:
            count += 1
        else:
            result.append(f"{current_char}{count}")
            current_char = sequence[i]
            count = 1
    
    result.append(f"{current_char}{count}")
    return "".join(result)

if __name__ == '__main__':
    sample_input = "wwwwaaadexxxxxx"
    compressed_output = compress_sequence(sample_input)
    print(compressed_output)