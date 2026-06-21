import itertools

def compress_string(s):
    if not s:
        return ""
    result = []
    for char, group in itertools.groupby(s):
        count = sum(1 for _ in group)
        result.append(f"{char}{count}")
    return "".join(result)

if __name__ == "__main__":
    sample_input = "aaabbbcccaaabbc"
    print(compress_string(sample_input))