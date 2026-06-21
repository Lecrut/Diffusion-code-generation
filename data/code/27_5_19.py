def rle_encode(data):
    if not data:
        return ""
    
    chars = list(data)
    shifted = [None] + chars[:-1]
    
    result = []
    current_char = chars[0]
    count = 1
    
    for i in range(1, len(chars)):
        if chars[i] == current_char:
            count += 1
        else:
            result.append(f"{current_char}{count}")
            current_char = chars[i]
            count = 1
    
    result.append(f"{current_char}{count}")
    return "".join(result)

if __name__ == '__main__':
    sample_input = "AAAAABBBB"
    encoded_result = rle_encode(sample_input)
    print(encoded_result)