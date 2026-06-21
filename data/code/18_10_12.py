import itertools

def run_length_encode(text):
    return [(char, len(list(group))) for char, group in itertools.groupby(text)]

if __name__ == '__main__':
    result = run_length_encode("AAABBC")
    print(result)