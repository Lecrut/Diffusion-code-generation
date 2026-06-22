def rle_compress(data):
    if not data:
        return ""
    
    compressed = []
    current_char = data[0]
    count = 1
    
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            if count > 1:
                compressed.append(str(count))
            compressed.append(current_char)
            current_char = data[i]
            count = 1
    
    if count > 1:
        compressed.append(str(count))
    compressed.append(current_char)
    
    return "".join(compressed)

if __name__ == "__main__":
    sample_string = "AAABBBCCCDAA"
    result = rle_compress(sample_string)
    print(result)