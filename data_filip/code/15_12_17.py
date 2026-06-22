import itertools

def compress_sequence(s: str) -> str:
    compressed = []
    for char, group in itertools.groupby(s):
        length = len(list(group))
        if length > 1:
            compressed.append(f"{length}{char}")
        else:
            compressed.append(char)
    return "".join(compressed)

if __name__ == '__main__':
    print(compress_sequence("AAABBBCCD"))