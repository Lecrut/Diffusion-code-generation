import itertools

def compress_sequence(sequence):
    if not sequence:
        return ""
    result = []
    for key, group in itertools.groupby(sequence):
        count = sum(1 for _ in group)
        result.append(f"{count}{key}")
    return "".join(result)

if __name__ == '__main__':
    sample_string = "aaabbbcccaa"
    print(compress_sequence(sample_string))