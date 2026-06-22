def split_csv_string(s):
    if not s:
        return []
    
    segments = []
    current = []
    i = 0
    n = len(s)
    
    while i < n:
        char = s[i]
        if char == ',':
            if current:
                segments.append(''.join(current))
                current = []
        else:
            current.append(char)
        i += 1
    
    if current:
        segments.append(''.join(current))
    
    return segments

if __name__ == '__main__':
    sample = "a,,b,,,c"
    result = split_csv_string(sample)
    print(result)