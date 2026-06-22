def run_length_encode(text):
    if not text:
        return ""
    
    encoded = []
    count = 1
    current_char = text[0]
    
    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            encoded.append(str(count))
            encoded.append(current_char)
            current_char = text[i]
            count = 1
            
    encoded.append(str(count))
    encoded.append(current_char)
    
    return "".join(encoded)

if __name__ == '__main__':
    sample_string = "aaabbbccca"
    result = run_length_encode(sample_string)
    print(result)