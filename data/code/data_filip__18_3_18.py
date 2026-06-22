from itertools import groupby

def rle_encode(s):
    if not s:
        return ""
    parts = []
    for char, group in groupby(s):
        count = sum(1 for _ in group)
        if count == 1:
            parts.append(char)
        else:
            parts.append(f"{count}{char}")
    return "".join(parts)

if __name__ == '__main__':
    text = "aaabbbcccc"
    print(rle_encode(text))