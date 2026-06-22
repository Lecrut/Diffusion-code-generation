import itertools

def compress_sequence(s):
    if not s:
        return ""
    result = []
    for key, group in itertools.groupby(s):
        count = sum(1 for _ in group)
        if count == 1:
            result.append(key)
        else:
            result.append(f"{count}{key}")
    return "".join(result)

if __name__ == '__main__':
    test_string = "aaabbcccdddd"
    compressed = compress_sequence(test_string)
    print(compressed)