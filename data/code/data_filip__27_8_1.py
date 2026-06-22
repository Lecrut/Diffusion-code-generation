def encode_rle(data: str) -> str:
    if not data:
        return ""
    
    result_parts = []
    current_char = data[0]
    count = 1
    
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            result_parts.append(f"{current_char}{count}")
            current_char = data[i]
            count = 1
    
    result_parts.append(f"{current_char}{count}")
    
    return "".join(result_parts)

if __name__ == '__main__':
    sample_input = 'WWWWWWWWWWWWWBWWWWWWWWWWWWWWWBWWWWWWWWWWWWWWCCCCCCCCCC'
    encoded_result = encode_rle(sample_input)
    print(encoded_result)