import itertools

def run_length_encode(text):
    if not text:
        return []
    return [(char, len(list(group))) for char, group in itertools.groupby(text)]

if __name__ == '__main__':
    encoded = run_length_encode("AAABBBCCC")
    print(encoded)