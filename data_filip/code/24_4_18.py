from itertools import groupby

def rle_compress(data: str) -> str:
    if not data:
        return ""
    compressed = []
    for char, group in groupby(data):
        count = sum(1 for _ in group)
        compressed.append(f"{char}{count}" if count > 1 else char)
    return "".join(compressed)

if __name__ == '__main__':
    sample_string = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
    result = rle_compress(sample_string)
    print(result)