def compress_string(s):
    if not s:
        return ""
    
    result = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append(f"{current_char}{count}")
            current_char = s[i]
            count = 1
    
    result.append(f"{current_char}{count}")
    return "".join(result)

if __name__ == "__main__":
    sample_string = "AAABBBCCCDDE"
    compressed_result = compress_string(sample_string)
    print(compressed_result)
    another_sample = "XYZ"
    another_result = compress_string(another_sample)
    print(another_result)
    empty_sample = ""
    empty_result = compress_string(empty_sample)
    print(empty_result)