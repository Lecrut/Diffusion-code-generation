import itertools

def compress_string(s):
    if not s:
        return ""
    groups = itertools.groupby(s)
    compressed_parts = []
    for char, group in groups:
        count = sum(1 for _ in group)
        compressed_parts.append(f"{count}{char}")
    return "".join(compressed_parts)

if __name__ == '__main__':
    sample_inputs = ["AAABBBCCD", "ABCDE", "A", "", "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"]
    for sample in sample_inputs:
        result = compress_string(sample)
        print(result)