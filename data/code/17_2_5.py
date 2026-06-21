from itertools import groupby

def compress_string(input_str):
    if not input_str:
        return ""
    compressed_parts = []
    for char, group in groupby(input_str):
        count = len(list(group))
        if count > 1:
            compressed_parts.append(f"{char}{count}")
        else:
            compressed_parts.append(char)
    return "".join(compressed_parts)

if __name__ == '__main__':
    sample_input = "aaabbbccdeee"
    result = compress_string(sample_input)
    print(result)