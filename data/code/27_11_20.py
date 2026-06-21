def rle_encode(text):
    if not text:
        return ""
    
    encoded = []
    count = 1
    current_char = text[0]
    
    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            encoded.append(str(count) + current_char)
            current_char = text[i]
            count = 1
    
    encoded.append(str(count) + current_char)
    return "".join(encoded)

if __name__ == '__main__':
    sample_text_1 = "AAABBBCCD"
    sample_text_2 = ""
    sample_text_3 = "A"
    sample_text_4 = "ABABAB"
    
    result_1 = rle_encode(sample_text_1)
    print(result_1)
    
    result_2 = rle_encode(sample_text_2)
    print(result_2)
    
    result_3 = rle_encode(sample_text_3)
    print(result_3)
    
    result_4 = rle_encode(sample_text_4)
    print(result_4)