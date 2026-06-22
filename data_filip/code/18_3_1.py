import itertools

def run_length_encode(s):
    encoded = []
    for char, group in itertools.groupby(s):
        count = sum(1 for _ in group)
        encoded.append(f"{count}{char}")
    return ''.join(encoded)

if __name__ == '__main__':
    sample = "aabbbccca"
    print(run_length_encode(sample))