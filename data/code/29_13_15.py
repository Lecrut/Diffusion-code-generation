import itertools

def compress_string(s):
    if not s:
        return ""
    parts = []
    for key, group in itertools.groupby(s):
        count = sum(1 for _ in group)
        if count == 1:
            parts.append(key)
        else:
            parts.append(f"{count}{key}")
    return "".join(parts)

if __name__ == '__main__':
    print(compress_string("aaabbcccdd"))