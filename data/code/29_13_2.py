from itertools import groupby

def compress_string(s):
    if not s:
        return ""
    result = []
    for char, group in groupby(s):
        count = sum(1 for _ in group)
        result.append(f"{count}{char}")
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbccccdd"
    output = compress_string(sample_input)
    print(output)