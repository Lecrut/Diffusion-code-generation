import itertools

def compress_string(s):
    if not s:
        return ""
    compressed = []
    for char, group in itertools.groupby(s):
        count = sum(1 for _ in group)
        compressed.append(f"{char}{count}")
    return "".join(compressed)

if __name__ == "__main__":
    sample_input = "aaabbbcccaaa"
    result = compress_string(sample_input)
    print(result)