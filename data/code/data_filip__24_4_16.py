import itertools

def compress_rle(input_string):
    if not input_string:
        return ""
    
    compressed = []
    for char, group in itertools.groupby(input_string):
        count = len(list(group))
        compressed.append(f"{count}{char}")
    
    return "".join(compressed)

if __name__ == '__main__':
    sample_string = "AAAABBBCCDAA"
    result = compress_rle(sample_string)
    print(result)