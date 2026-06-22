def compress_string(s: str) -> str:
    if not s:
        return ""
    chars = list(s)
    result = []
    i = 0
    n = len(chars)
    while i < n:
        current_char = chars[i]
        count = 1
        while i + 1 < n and chars[i + 1] == current_char:
            i += 1
            count += 1
        result.append(f"{current_char}{count}")
        i += 1
    return "".join(result)

if __name__ == '__main__':
    sample_input = 'bbbaaa'
    print(compress_string(sample_input))