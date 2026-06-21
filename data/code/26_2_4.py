def run_length_encode(s):
    if not s:
        return []
    
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

if __name__ == '__main__':
    print(run_length_encode("AAABBBCCDA"))
    print(run_length_encode("ABABAB"))
    print(run_length_encode(""))
    print(run_length_encode("Z"))
    print(run_length_encode("AABBCC"))