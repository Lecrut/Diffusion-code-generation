def run_length_encode(s: str) -> str:
    if not s:
        return ""
    
    if len(s) == 1:
        return "1" + s
    
    result = []
    i = 0
    n = len(s)
    
    while i < n:
        char = s[i]
        count = 1
        j = i + 1
        while j < n and s[j] == char:
            count += 1
            j += 1
        if count > 1:
            result.append(str(count))
        result.append(char)
        i = j
        
    return "".join(result)

def run_length_decode(s: str) -> str:
    if not s:
        return ""
    
    result = []
    i = 0
    n = len(s)
    
    while i < n:
        count_str = []
        while i < n and s[i].isdigit():
            count_str.append(s[i])
            i += 1
        
        if count_str:
            count = int("".join(count_str))
        else:
            count = 1
            
        if i < n:
            char = s[i]
            result.append(char * count)
            i += 1
            
    return "".join(result)

if __name__ == '__main__':
    original = "aaabbc"
    encoded = run_length_encode(original)
    decoded = run_length_decode(encoded)
    print(encoded)
    print(decoded)