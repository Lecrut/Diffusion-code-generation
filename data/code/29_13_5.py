import itertools

def compress_string(data):
    if not data:
        return ""
    result = []
    for char, group in itertools.groupby(data):
        count = sum(1 for _ in group)
        result.append(f"{count}{char}")
    return "".join(result)

if __name__ == '__main__':
    sample = "aaabbccccd"
    compressed = compress_string(sample)
    print(compressed)