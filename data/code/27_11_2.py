def rle_encode(text: str) -> str:
    if not text:
        return ""
    
    result = []
    count = 0
    prev_char = text[0]
    
    for char in text[1:]:
        if char == prev_char:
            count += 1
        else:
            result.append(f"{count}{prev_char}")
            prev_char = char
            count = 1
    result.append(f"{count}{prev_char}")
    
    return "".join(result)

if __name__ == '__main__':
    sample_text = "AAABBBCCD"
    encoded_result = rle_encode(sample_text)
    print(encoded_result)