def run_length_encode(s: str) -> str:
    if not s:
        return ""
    
    compressed = []
    count = 1
    current_char = s[0]
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            compressed.append(f"{current_char}{count}")
            current_char = s[i]
            count = 1
    compressed.append(f"{current_char}{count}")
    
    result = "".join(compressed)
    return result if len(result) < len(s) else s

if __name__ == '__main__':
    sample = "aabcccccaaa"
    result = run_length_encode(sample)
    print(result)
    
    sample_empty = ""
    result_empty = run_length_encode(sample_empty)
    print(result_empty)
    
    sample_no_compress = "abcde"
    result_no_compress = run_length_encode(sample_no_compress)
    print(result_no_compress)