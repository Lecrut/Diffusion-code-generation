def compress_string(s: str) -> str:
    if not s:
        return ""
    
    result = []
    current_char = s[0]
    count = 1
    
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            if count > 1:
                result.append(f"{current_char}{count}")
            else:
                result.append(current_char)
            current_char = char
            count = 1
    
    if count > 1:
        result.append(f"{current_char}{count}")
    else:
        result.append(current_char)
    
    return "".join(result)

if __name__ == '__main__':
    samples = [
        "aaabbccccd",
        "abc",
        "aabbcc",
        "aaaaa",
        "",
        "hello"
    ]
    for sample in samples:
        print(compress_string(sample))