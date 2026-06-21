from itertools import groupby

def compress_string(s):
    if not s:
        return ""
    result = []
    for char, group in groupby(s):
        count = sum(1 for _ in group)
        result.append(f"{char}{count}")
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbccccd"
    compressed_output = compress_string(sample_input)
    print(compressed_output)