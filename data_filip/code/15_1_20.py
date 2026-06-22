def compress_string(s):
    if not s:
        return ""
    
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(f"{s[i - 1]}{count}")
            count = 1
    result.append(f"{s[-1]}{count}")
    
    compressed = "".join(result)
    return compressed if len(compressed) < len(s) else s

if __name__ == '__main__':
    sample = 'aaaaabbbbcccd'
    output = compress_string(sample)
    print(output)