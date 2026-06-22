def rle_compress(input_string):
    if not input_string:
        return ""
    
    compressed = []
    count = 1
    current_char = input_string[0]
    
    for i in range(1, len(input_string)):
        if input_string[i] == current_char:
            count += 1
        else:
            if count > 1:
                compressed.append(str(count))
            compressed.append(current_char)
            current_char = input_string[i]
            count = 1
    
    if count > 1:
        compressed.append(str(count))
    compressed.append(current_char)
    
    return "".join(compressed)

if __name__ == '__main__':
    text = "aaabbccccdd"
    result = rle_compress(text)
    print(result)