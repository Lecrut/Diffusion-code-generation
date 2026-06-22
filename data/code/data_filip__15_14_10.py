import itertools

def compress_string(s):
    if not s:
        return ""
    result = []
    for char, group in itertools.groupby(s):
        count = len(list(group))
        result.append(f"{char}{count}")
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbbaaccc"
    compressed_result = compress_string(sample_input)
    print(compressed_result)
    sample_empty = ""
    print(compress_string(sample_empty))
    sample_single = "z"
    print(compress_string(sample_single))