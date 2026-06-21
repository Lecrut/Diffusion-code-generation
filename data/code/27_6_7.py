def rle_encode(s: str) -> list:
    if not s:
        return []
    result = []
    current_char = s[0]
    count = 1
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append((count, current_char))
            current_char = s[i]
            count = 1
    result.append((count, current_char))
    return result

if __name__ == '__main__':
    sample = "AAABBBCCD"
    print(rle_encode(sample))