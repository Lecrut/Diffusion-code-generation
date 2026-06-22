def compress_string(s):
    if not s:
        return ""
    if len(s) <= 1:
        return f"{s}1"
    
    result = []
    count = 1
    current_char = s[0]
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append(f"{current_char}{count}")
            current_char = s[i]
            count = 1
    result.append(f"{current_char}{count}")
    
    return "".join(result)

def run():
    s = "aabcccccaaa"
    compressed = compress_string(s)
    if len(compressed) < len(s):
        print(compressed)
    else:
        print(s)

if __name__ == '__main__':
    run()