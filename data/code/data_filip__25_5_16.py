import itertools

def run_length_encode(s):
    return ''.join(f"{len(list(g))}{k}" for k, g in itertools.groupby(s))

if __name__ == '__main__':
    print(run_length_encode("aaabbc"))
    print(run_length_encode("xyz"))
    print(run_length_encode("aabbaaaccc"))