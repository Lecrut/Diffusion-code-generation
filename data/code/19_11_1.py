def rle_encode(data):
    if not data:
        return ""
    
    encoded = []
    prev_char = data[0]
    count = 1
    
    for i in range(1, len(data)):
        char = data[i]
        if char == prev_char:
            count += 1
        else:
            encoded.append(str(count))
            encoded.append(prev_char)
            prev_char = char
            count = 1
            
    encoded.append(str(count))
    encoded.append(prev_char)
    
    return "".join(encoded)

if __name__ == '__main__':
    sample_string = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    result = rle_encode(sample_string)
    print(result)