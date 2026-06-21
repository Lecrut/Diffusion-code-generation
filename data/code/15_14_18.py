import itertools

def compress_string(s):
    if not s:
        return ""
    compressed = []
    for char, group in itertools.groupby(s):
        count = sum(1 for _ in group)
        if count > 1:
            compressed.append(f"{char}{count}")
        else:
            compressed.append(char)
    return "".join(compressed)

if __name__ == '__main__':
    sample_inputs = [
        "aaabbcccc",
        "hello",
        "aabbcc",
        "abcdef",
        "",
        "a"
    ]
    for sample in sample_inputs:
        result = compress_string(sample)
        print(f"compress_string({sample!r}) -> {result!r}")