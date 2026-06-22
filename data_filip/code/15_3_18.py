def compress_string(s):
    if not s: return ""
    result, current_char, count = [], s[0], 1
    for char in s[1:]:
        if char == current_char: count += 1
        else: result.append(f"{count}{current_char}"); current_char, count = char, 1
    result.append(f"{count}{current_char}")
    return "".join(result)

if __name__ == '__main__':
    sample = 'bbbaaa'
    print(compress_string(sample))