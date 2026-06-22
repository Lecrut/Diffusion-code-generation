def encode_repeated_chars(s):
    if not s:
        return
    i = 0
    n = len(s)
    while i < n:
        char = s[i]
        count = 1
        j = i + 1
        while j < n and s[j] == char:
            count += 1
            j += 1
        yield f"{count}{char}"
        i = j

if __name__ == '__main__':
    text = "aaabbc"
    result = list(encode_repeated_chars(text))
    print(result)