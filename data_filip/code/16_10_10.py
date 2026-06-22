def rle_encode(s: str) -> str:
    if not s:
        return ""
    
    result = []
    count = 1
    n = len(s)
    
    for i in range(1, n):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(str(count))
            result.append(s[i - 1])
            count = 1
    result.append(str(count))
    result.append(s[n - 1])
    
    return "".join(result)

def rle_decode(s: str) -> str:
    if not s:
        return ""
    
    result = []
    n = len(s)
    i = 0
    
    while i < n:
        digit = s[i]
        count = int(digit)
        i += 1
        char = s[i]
        i += 1
        result.append(char * count)
    
    return "".join(result)

if __name__ == '__main__':
    original = "AAABBBCCDAA"
    encoded = rle_encode(original)
    decoded = rle_decode(encoded)
    
    print(encoded)
    print(decoded)