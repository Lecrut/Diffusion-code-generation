def compress_string(text):
    if not text:
        return ""
    
    result = []
    current_char = text[0]
    count = 1
    
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(current_char + str(count))
            current_char = char
            count = 1
    result.append(current_char + str(count))
    
    return "".join(result)

if __name__ == '__main__':
    sample = "aabcccccaaa"
    compressed = compress_string(sample)
    print(compressed)