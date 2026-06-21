def rle_encode(data):
    if not data:
        return ""
    
    result = []
    length = len(data)
    index = 0
    
    while index < length:
        count = 1
        current_char = data[index]
        index += 1
        
        while index < length and data[index] == current_char:
            count += 1
            index += 1
        
        result.append(f"{current_char}{count}")
    
    return "".join(result)

if __name__ == '__main__':
    sample_string = 'WWWWWWWWWWWWWBWWWWWWWWWWWWWWWBWWWWWWWWWWWWWWCCCCCCCCCC'
    encoded_data = rle_encode(sample_string)
    print(encoded_data)