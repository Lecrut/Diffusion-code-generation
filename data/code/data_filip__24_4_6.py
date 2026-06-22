import itertools

def compress_rle(data):
    if not data:
        return ""
    compressed = []
    for key, group in itertools.groupby(data):
        count = sum(1 for _ in group)
        compressed.append(f"{key}{count}")
    return "".join(compressed)

if __name__ == "__main__":
    sample_string = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    result = compress_rle(sample_string)
    print(result)