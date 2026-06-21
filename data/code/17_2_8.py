import itertools

def compress_string(s: str) -> str:
    if not s:
        return ""
    result = []
    for char, group in itertools.groupby(s):
        count = len(list(group))
        if count > 1:
            result.append(f"{char}{count}")
        else:
            result.append(char)
    return "".join(result)

if __name__ == "__main__":
    sample_input = "aaabbccccdd"
    compressed_output = compress_string(sample_input)
    print(compressed_output)