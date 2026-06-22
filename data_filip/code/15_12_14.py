import itertools

def compress_string(input_string):
    if not input_string:
        return ""
    compressed_parts = []
    for key, group in itertools.groupby(input_string):
        count = len(list(group))
        if count == 1:
            compressed_parts.append(key)
        else:
            compressed_parts.append(f"{key}{count}")
    return "".join(compressed_parts)

if __name__ == '__main__':
    test_data = "aaabbbcccaaa"
    result = compress_string(test_data)
    print(result)