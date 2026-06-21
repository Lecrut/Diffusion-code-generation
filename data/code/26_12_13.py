def compress_string(s: str) -> str:
    if not s:
        return ""
    
    if len(s) == 1:
        return s
    
    encoded = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            encoded.append(s[i - 1])
            encoded.append(str(count))
            count = 1
    
    encoded.append(s[-1])
    encoded.append(str(count))
    
    result = "".join(encoded)
    
    if len(result) >= len(s):
        return s
    
    return result

if __name__ == '__main__':
    sample_inputs = ["aaabbcccc", "", "abc", "a", "aaaaaa"]
    for s in sample_inputs:
        result = compress_string(s)
        print(result)