def compress_string(s: str) -> str:
    if not s:
        return ""
    
    compressed = []
    count = 1
    prev_char = s[0]
    
    for char in s[1:]:
        if char == prev_char:
            count += 1
        else:
            compressed.append(f"{prev_char}{count}")
            prev_char = char
            count = 1
    
    compressed.append(f"{prev_char}{count}")
    
    return "".join(compressed)

if __name__ == '__main__':
    input_str = 'cccccccccc'
    result = compress_string(input_str)
    print(result)