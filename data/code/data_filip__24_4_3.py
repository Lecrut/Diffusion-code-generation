import itertools

def rle_compress(data):
    if not data:
        return ""
    result = []
    for char, group in itertools.groupby(data):
        count = sum(1 for _ in group)
        result.append(f"{char}{count}")
    return "".join(result)

if __name__ == '__main__':
    sample_string = "AAABBBCCCCDDDEEEEEFFFFFF"
    compressed_output = rle_compress(sample_string)
    print(compressed_output)