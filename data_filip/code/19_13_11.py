def run_length_encode(sequence):
    if not sequence:
        return ""
    
    encoded = []
    current_char = sequence[0]
    count = 1
    
    for char in sequence[1:]:
        if char == current_char:
            count += 1
        else:
            if count > 1:
                encoded.append(str(count))
            encoded.append(current_char)
            current_char = char
            count = 1
    
    if count > 1:
        encoded.append(str(count))
    encoded.append(current_char)
    
    return "".join(encoded)

if __name__ == '__main__':
    sample_sequences = [
        "AAABBBDD",
        "ABC",
        "AAAAAAAAAA",
        "AABBCC",
        "",
        "XYZXYZ"
    ]
    
    for seq in sample_sequences:
        result = run_length_encode(seq)
        print(result)