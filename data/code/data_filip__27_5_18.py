def rle_encode(s):
    if not s:
        return ""
    encoded = []
    count = 1
    for current, next_char in zip(s, s[1:]):
        if current == next_char:
            count += 1
        else:
            encoded.append(f"{count}{current}")
            count = 1
    encoded.append(f"{count}{s[-1]}")
    return "".join(encoded)

if __name__ == '__main__':
    sample = 'AAAAABBBB'
    print(rle_encode(sample))