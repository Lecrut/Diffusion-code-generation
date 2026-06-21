from itertools import groupby

def run_length_encode(s):
    if not s:
        return ""
    result = []
    for char, group in groupby(s):
        count = sum(1 for _ in group)
        result.append(str(count) + char)
    return "".join(result)

if __name__ == '__main__':
    samples = [
        "aabbbcc",
        "abc",
        "aaaaabbbbbccccc",
        "",
        "a",
        "xyzzzaaa"
    ]
    for sample in samples:
        print(run_length_encode(sample))