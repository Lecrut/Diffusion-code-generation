def rle_encode(input_string):
    if not input_string:
        return ""
    
    result = []
    current_char = input_string[0]
    count = 1
    
    for i in range(1, len(input_string)):
        if input_string[i] == current_char:
            count += 1
        else:
            result.append(str(count))
            result.append(current_char)
            current_char = input_string[i]
            count = 1
            
    result.append(str(count))
    result.append(current_char)
    
    return "".join(result)

if __name__ == '__main__':
    original_text = "AAABBBCCCC"
    compressed_text = rle_encode(original_text)
    print(compressed_text)