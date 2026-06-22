from itertools import groupby

def rle_compress(s: str) -> str:
    result = []
    for key, group in groupby(s):
        count = len(list(group))
        if count == 1:
            result.append(key)
        else:
            result.append(f"{count}{key}")
    return "".join(result)

if __name__ == '__main__':
    sample_string = "AAABBBCCDAA"
    compressed = rle_compress(sample_string)
    print(compressed)