import itertools

def compress_rle(s):
    if not s:
        return ""
    result = []
    for key, group in itertools.groupby(s):
        count = len(list(group))
        result.append(f"{count}{key}")
    return "".join(result)

if __name__ == '__main__':
    sample_string = "aaabbcdd"
    print(compress_rle(sample_string))