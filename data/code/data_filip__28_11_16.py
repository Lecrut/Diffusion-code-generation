def run_length_encode(data):
    if not data:
        return ""
    
    if len(data) == 1:
        return "1" + data
    
    encoded = []
    count = 1
    current_char = data[0]
    
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            encoded.append(str(count))
            encoded.append(current_char)
            current_char = data[i]
            count = 1
    
    encoded.append(str(count))
    encoded.append(current_char)
    
    return "".join(encoded)

if __name__ == '__main__':
    sample_strings = [
        "",
        "A",
        "AAABBBCCC",
        "AABCCCC",
        "112233",
        "abcdef"
    ]
    
    for s in sample_strings:
        result = run_length_encode(s)
        print(result)