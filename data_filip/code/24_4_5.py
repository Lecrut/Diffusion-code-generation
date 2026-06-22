import itertools

def compress_rle(input_string: str) -> str:
    if not input_string:
        return ""
    
    compressed = []
    for key, group in itertools.groupby(input_string):
        count = len(list(group))
        compressed.append(f"{count}{key}")
    
    return "".join(compressed)

if __name__ == '__main__':
    sample_input = "AAABBBCCDAA"
    result = compress_rle(sample_input)
    print(result)