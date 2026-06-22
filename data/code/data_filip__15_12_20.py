import itertools

def compress_sequence(sequence: str) -> str:
    result = []
    for char, group in itertools.groupby(sequence):
        count = len(list(group))
        if count == 1:
            result.append(char)
        else:
            result.append(f"{char}{count}")
    return ''.join(result)

if __name__ == '__main__':
    test_string = "aaabbbcccd"
    compressed = compress_sequence(test_string)
    print(compressed)