import itertools

def compress_string(s):
    if not s:
        return ""
    parts = []
    for char, group in itertools.groupby(s):
        count = len(list(group))
        parts.append(f"{char}{count}")
    return "".join(parts)

if __name__ == '__main__':
    sample_input = "aaabbcdddd"
    result = compress_string(sample_input)
    print(result)