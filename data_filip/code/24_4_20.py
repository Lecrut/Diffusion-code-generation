import itertools

def compress_rle(data):
    if not data:
        return ""
    result = []
    for key, group in itertools.groupby(data):
        count = sum(1 for _ in group)
        result.append(f"{key}{count}")
    return "".join(result)

if __name__ == '__main__':
    sample_string = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    compressed = compress_rle(sample_string)
    print(compressed)