def rle_encode(data):
    if not data:
        return []
    
    encoded_list = []
    current_char = data[0]
    count = 1
    
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            encoded_list.append((count, current_char))
            current_char = data[i]
            count = 1
    
    encoded_list.append((count, current_char))
    return encoded_list

if __name__ == '__main__':
    sample_input = "aaabbbcccaaa"
    result = rle_encode(sample_input)
    print(result)