def run_length_encoding(data):
    if not data:
        return ""
    
    result = []
    count = 1
    current_char = data[0]
    
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = data[i]
            count = 1
    
    result.append(f"{count}{current_char}")
    return "".join(result)

if __name__ == '__main__':
    sample_string = "aaabbbccccddddeee"
    encoded_result = run_length_encoding(sample_string)
    print(encoded_result)