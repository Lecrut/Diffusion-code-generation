def compress_text(text):
    if not text:
        return ""
    
    result_parts = []
    i = 0
    n = len(text)
    
    while i < n:
        current_char = text[i]
        count = 1
        while i + count < n and text[i + count] == current_char:
            count += 1
        
        if count == 1:
            result_parts.append(current_char)
        else:
            result_parts.append(current_char)
            result_parts.append(str(count))
        
        i += count
    
    return "".join(result_parts)

if __name__ == "__main__":
    sample1 = "aabcccccaaa"
    sample2 = "abcdef"
    sample3 = "aabbcc"
    sample4 = ""
    sample5 = "aaaaa"
    
    print(compress_text(sample1))
    print(compress_text(sample2))
    print(compress_text(sample3))
    print(compress_text(sample4))
    print(compress_text(sample5))