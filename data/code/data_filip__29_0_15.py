def run_length_encode(text):
    if not text:
        return ""
    
    compressed = []
    current_char = text[0]
    count = 1
    
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            compressed.append(str(count))
            compressed.append(current_char)
            current_char = char
            count = 1
    
    compressed.append(str(count))
    compressed.append(current_char)
    
    return "".join(compressed)

if __name__ == '__main__':
    sample_string = "aaabbc"
    result = run_length_encode(sample_string)
    print(result)