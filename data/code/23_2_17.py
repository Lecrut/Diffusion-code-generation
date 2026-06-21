def rle_encode(s):
    if not s:
        return ""
    
    result = []
    count = 1
    current_char = s[0]
    
    for i in range(1, len(s)):
        char = s[i]
        if char == current_char:
            count += 1
        else:
            result.append(f"{current_char}{count}")
            current_char = char
            count = 1
    result.append(f"{current_char}{count}")
    return "".join(result)

def rle_decode(s):
    if not s:
        return ""
    
    result = []
    i = 0
    n = len(s)
    
    while i < n:
        char = s[i]
        i += 1
        num_str = ""
        while i < n and s[i].isdigit():
            num_str += s[i]
            i += 1
        count = int(num_str) if num_str else 1
        result.append(char * count)
    return "".join(result)

if __name__ == '__main__':
    encoded = rle_encode("AAABBBCCCD")
    print(encoded)
    
    decoded = rle_decode("A3B3C3D1")
    print(decoded)