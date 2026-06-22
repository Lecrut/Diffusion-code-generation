def rle_encode(s):
    if not s:
        return ""
    return "".join(f"{count}{char}" if count > 1 else f"{char}" for count, char in _compress(s))

def _compress(s):
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
    print(rle_encode("AAABBC"))
    print(rle_encode(""))
    print(rle_encode("A"))
    print(rle_encode("ABCD"))