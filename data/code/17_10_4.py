def rle_encode(text):
    if not text:
        return ""
    
    result = []
    current_char = text[0]
    count = 1
    
    iterator = iter(text)
    next(iterator)
    
    for char in iterator:
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1
    
    result.append(f"{count}{current_char}")
    return "".join(result)

if __name__ == '__main__':
    sample_text = "aabbbccccddd"
    encoded_result = rle_encode(sample_text)
    print(encoded_result)