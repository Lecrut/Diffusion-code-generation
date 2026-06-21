from itertools import groupby

def compress_sequence(input_string):
    if not input_string:
        return ""
    compressed_parts = []
    for char, group in groupby(input_string):
        count = sum(1 for _ in group)
        if count > 1:
            compressed_parts.append(f"{char}{count}")
        else:
            compressed_parts.append(char)
    return "".join(compressed_parts)

if __name__ == '__main__':
    test_string = "aaabbbccccddde"
    result = compress_sequence(test_string)
    print(result)