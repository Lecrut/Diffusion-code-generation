def run_length_encode(data: str) -> str:
    if not data:
        return ""
    
    encoded = []
    current_char = data[0]
    count = 1
    
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            encoded.append(f"{count}{current_char}")
            current_char = data[i]
            count = 1
    
    encoded.append(f"{count}{current_char}")
    return "".join(encoded)

if __name__ == '__main__':
    sample_string = "AAABBBCCCCDDDEEEFGGG"
    result = run_length_encode(sample_string)
    print(result)