import itertools

def run_length_encode(s):
    if not s:
        return []
    result = []
    for key, group in itertools.groupby(s):
        count = sum(1 for _ in group)
        result.append((key, count))
    return result

if __name__ == '__main__':
    sample_string = "AAABBBCCCDDDEEEFFFGGGHHHIIIIJJJKKKLLMMMMNNNNOOOOPPPQQQRRRSSSTTTUUUVVVWWWWWXYYYYZZZZZ"
    encoded = run_length_encode(sample_string)
    print(encoded)