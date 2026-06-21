import itertools

def compress_string(s: str) -> str:
    if not s:
        return ""
    parts = []
    for char, group in itertools.groupby(s):
        count = sum(1 for _ in group)
        parts.append(f"{count}{char}")
    return "".join(parts)

if __name__ == '__main__':
    sample = "aaabbc"
    result = compress_string(sample)
    print(result)