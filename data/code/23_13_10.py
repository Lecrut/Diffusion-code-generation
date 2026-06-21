def run_length_encode(text):
    if not text:
        return ""
    
    encoded_parts = []
    count = 1
    current_char = text[0]
    
    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            encoded_parts.append(f"{current_char}{count}")
            current_char = text[i]
            count = 1
    
    encoded_parts.append(f"{current_char}{count}")
    
    return "".join(encoded_parts)

if __name__ == '__main__':
    sample_string = "AAAABBBCCDAA"
    result = run_length_encode(sample_string)
    print(result)