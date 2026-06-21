from itertools import groupby

def compress_sequence(sequence: str) -> str:
    if not sequence:
        return ""
    segments = []
    for key, group in groupby(sequence):
        count = len(list(group))
        segments.append(key + str(count))
    return "".join(segments)

if __name__ == '__main__':
    test_data = 'zzzbbbccddddeee'
    output = compress_sequence(test_data)
    print(output)