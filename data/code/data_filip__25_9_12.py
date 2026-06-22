def rle_encode_mem_efficient(text):
    if not text:
        return ""
    
    result_parts = []
    current_char = text[0]
    count = 1
    
    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            result_parts.append(str(count))
            result_parts.append(current_char)
            current_char = text[i]
            count = 1
    
    result_parts.append(str(count))
    result_parts.append(current_char)
    
    return "".join(result_parts)

if __name__ == '__main__':
    sample_string = "AAABBBCCCCCDDDDDDDDDDD"
    encoded = rle_encode_mem_efficient(sample_string)
    print(encoded)