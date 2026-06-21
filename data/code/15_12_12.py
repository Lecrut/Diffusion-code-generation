import itertools

def compress_sequence(s):
    result = []
    for key, group in itertools.groupby(s):
        count = len(list(group))
        if count == 1:
            result.append(key)
        else:
            result.append(f"{count}{key}")
    return "".join(result)

if __name__ == '__main__':
    test_string = "aaabbccc"
    compressed = compress_sequence(test_string)
    print(compressed)