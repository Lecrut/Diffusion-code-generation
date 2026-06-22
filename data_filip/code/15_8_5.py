def encode_adjacent(s):
    if not s:
        return ""
    chars = [s[0]]
    counts = [1]
    for c in s[1:]:
        if c == chars[-1]:
            counts[-1] += 1
        else:
            chars.append(c)
            counts.append(1)
    return "".join(f"{ch}{ct}" for ch, ct in zip(chars, counts))

if __name__ == '__main__':
    print(encode_adjacent("hello"))