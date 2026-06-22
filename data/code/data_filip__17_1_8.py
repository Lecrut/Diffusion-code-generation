def run_length_encode(s):
    if not s:
        return ""
    
    result = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = s[i]
            count = 1
    
    result.append((current_char, count))
    return result

def format_rle(rle_list):
    parts = []
    for char, count in rle_list:
        if count == 1:
            parts.append(char)
        else:
            parts.append(f"{count}{char}")
    return "".join(parts)

if __name__ == '__main__':
    sample1 = "AABCCCDD"
    rle1 = run_length_encode(sample1)
    print(format_rle(rle1))
    
    sample2 = ""
    rle2 = run_length_encode(sample2)
    print(format_rle(rle2))
    
    sample3 = "Z"
    rle3 = run_length_encode(sample3)
    print(format_rle(rle3))
    
    sample4 = "AAABBBCCC"
    rle4 = run_length_encode(sample4)
    print(format_rle(rle4))
    
    sample5 = "ABCDE"
    rle5 = run_length_encode(sample5)
    print(format_rle(rle5))