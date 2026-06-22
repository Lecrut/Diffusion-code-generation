from itertools import groupby

def compress_string_rle(data):
    if not data:
        return ""
    result = []
    for key, group in groupby(data):
        count = sum(1 for _ in group)
        result.append(f"{key}{count}")
    return "".join(result)

if __name__ == "__main__":
    sample_input = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    compressed_output = compress_string_rle(sample_input)
    print(compressed_output)