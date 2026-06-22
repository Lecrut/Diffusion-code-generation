import itertools

def compress_sequence(s):
    if not s:
        return ""
    result = []
    for char, group in itertools.groupby(s):
        count = sum(1 for _ in group)
        result.append(f"{char}{count}" if count > 1 else char)
    return "".join(result)

if __name__ == '__main__':
    test_string = "aaabbcdddddeff"
    compressed = compress_sequence(test_string)
    print(compressed)