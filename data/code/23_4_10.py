def rle_encode(data):
    if not data:
        return ""
    
    encoded = []
    current_char = data[0]
    count = 1
    
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            encoded.append(current_char)
            encoded.append(str(count))
            current_char = data[i]
            count = 1
    
    encoded.append(current_char)
    encoded.append(str(count))
    
    return "".join(encoded)

if __name__ == '__main__':
    sample_input = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    result = rle_encode(sample_input)
    print(result)
    
    sample_input2 = "AAABBBCCCCDDD"
    result2 = rle_encode(sample_input2)
    print(result2)
    
    sample_input3 = "A"
    result3 = rle_encode(sample_input3)
    print(result3)
    
    sample_input4 = ""
    result4 = rle_encode(sample_input4)
    print(f"'{result4}'")
    
    sample_input5 = "AABBBCCCCCCCCCDDDDDDDDDDD"
    result5 = rle_encode(sample_input5)
    print(result5)