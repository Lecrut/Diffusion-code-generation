import itertools

def compress_sequence(text):
    result = []
    for char, group in itertools.groupby(text):
        count = len(list(group))
        if count == 1:
            result.append(char)
        else:
            result.append(f"{count}{char}")
    return ''.join(result)

if __name__ == '__main__':
    test_string = "aaabbccccddddd"
    compressed = compress_sequence(test_string)
    print(compressed)