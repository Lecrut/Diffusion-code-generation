import itertools

def compress_rle(input_string: str) -> str:
    if not input_string:
        return ""
    
    result = []
    for key, group in itertools.groupby(input_string):
        count = sum(1 for _ in group)
        result.append(f"{count}{key}")
    
    return "".join(result)

if __name__ == '__main__':
    sample_input = "AAABBBCCCD"
    compressed = compress_rle(sample_input)
    print(compressed)