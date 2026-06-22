def run_length_encode(s: str) -> str:
    if not s:
        return s
    
    if len(s) == 1:
        return s
    
    result = []
    count = 1
    current_char = s[0]
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            if count > 1:
                result.append(str(count))
            result.append(current_char)
            current_char = s[i]
            count = 1
    
    if count > 1:
        result.append(str(count))
    result.append(current_char)
    
    compressed = ''.join(result)
    
    if len(compressed) >= len(s):
        return s
    
    return compressed

if __name__ == '__main__':
    print(run_length_encode("aaabbc"))
    print(run_length_encode("abcdef"))
    print(run_length_encode(""))
    print(run_length_encode("a"))