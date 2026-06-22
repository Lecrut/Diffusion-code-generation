def rle_encode_case_insensitive(s):
    if not s:
        return ""
    
    s = s.lower()
    result = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            if count > 1:
                result.append(f"{current_char}{count}")
            else:
                result.append(current_char)
            current_char = s[i]
            count = 1
    
    if count > 1:
        result.append(f"{current_char}{count}")
    else:
        result.append(current_char)
    
    return "".join(result)

if __name__ == '__main__':
    sample1 = "AAaaBBbBCCcc"
    sample2 = "aAbBcC"
    sample3 = ""
    sample4 = "Hello World!!"
    
    print(rle_encode_case_insensitive(sample1))
    print(rle_encode_case_insensitive(sample2))
    print(rle_encode_case_insensitive(sample3))
    print(rle_encode_case_insensitive(sample4))