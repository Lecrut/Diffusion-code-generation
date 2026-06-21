import io

def rle_encode(s):
    if not s:
        return ""
    
    chunks = []
    buffer = io.StringIO()
    
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        char = s[i]
        if char == current_char:
            count += 1
        else:
            chunks.append((current_char, count))
            current_char = char
            count = 1
    
    chunks.append((current_char, count))
    
    for char, count in chunks:
        buffer.write(str(count))
        buffer.write(char)
    
    return buffer.getvalue()

if __name__ == '__main__':
    sample = "AAAABBBCCDAA"
    result = rle_encode(sample)
    print(result)