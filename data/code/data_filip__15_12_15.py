import itertools

def compress_sequence(text: str) -> str:
    if not text:
        return ""
    result = []
    for char, group in itertools.groupby(text):
        count = len(list(group))
        if count == 1:
            result.append(char)
        else:
            result.append(f"{char}{count}")
    return "".join(result)

if __name__ == '__main__':
    sample = "aaabbcddde"
    compressed = compress_sequence(sample)
    print(compressed)