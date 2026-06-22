def rle_encode(sequence: str) -> str:
    if not sequence:
        return ""
    
    encoded = []
    current_char = sequence[0]
    count = 1
    
    for char in sequence[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append(f"{count}{current_char}")
            current_char = char
            count = 1
    
    encoded.append(f"{count}{current_char}")
    
    return "".join(encoded)

if __name__ == '__main__':
    sequence = "aabcccccaaa"
    result = rle_encode(sequence)
    print(result)