def compress_rle(text: str) -> str:
    if not text:
        return ""
    
    result = []
    count = 1
    current_char = text[0]
    
    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            if count >= 3:
                result.append(f"{current_char}{count}")
            elif count == 2:
                result.append(current_char * 2)
            else:
                result.append(current_char)
            current_char = text[i]
            count = 1
    
    if count >= 3:
        result.append(f"{current_char}{count}")
    elif count == 2:
        result.append(current_char * 2)
    else:
        result.append(current_char)
    
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbcdeeeeefffffg"
    compressed_result = compress_rle(sample_input)
    print(f"Input: {sample_input}")
    print(f"Output: {compressed_result}")