def rle_encode(data):
    if not data:
        return ""
    
    encoded_parts = []
    i = 0
    n = len(data)
    
    while i < n:
        count = 1
        while i + 1 < n and data[i] == data[i + 1]:
            count += 1
            i += 1
        
        encoded_parts.append(str(count) + data[i])
        i += 1
    
    return "".join(encoded_parts)

if __name__ == '__main__':
    sample_input = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    result = rle_encode(sample_input)
    print(result)