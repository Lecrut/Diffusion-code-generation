import itertools

def compress_rle(data):
    return "".join(f"{count}{char}" for char, group in itertools.groupby(data) for count in (sum(1 for _ in group),) if count > 0)

def decompress_rle(data):
    result = []
    i = 0
    while i < len(data):
        char = data[i]
        i += 1
        count_str = ""
        while i < len(data) and data[i].isdigit():
            count_str += data[i]
            i += 1
        count = int(count_str)
        result.append(char * count)
    return "".join(result)

if __name__ == "__main__":
    sample_string = "AAAABBBBCCCCDDDDDD"
    compressed = compress_rle(sample_string)
    decompressed = decompress_rle(compressed)
    print(compressed)
    print(decompressed)