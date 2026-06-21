import itertools

def compress_sequence(input_string):
    if not input_string:
        return ""
    result = []
    for char, group in itertools.groupby(input_string):
        count = len(list(group))
        if count > 1:
            result.append(f"{char}{count}")
        else:
            result.append(char)
    return "".join(result)

if __name__ == '__main__':
    test_string = "aaabbbccdddeeeefffggg"
    compressed = compress_sequence(test_string)
    print(compressed)