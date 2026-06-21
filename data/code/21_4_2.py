def rle_encode(text):
    if not text:
        return {}
    
    result = {}
    current_char = text[0]
    count = 1
    
    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            result[current_char] = count
            current_char = text[i]
            count = 1
            
    result[current_char] = count
    return result

if __name__ == '__main__':
    sample_string = "aaabbbcc"
    encoded = rle_encode(sample_string)
    print(encoded)