import itertools

def run_length_encode(s):
    if not s:
        return []

    def make_group(g):
        return (g[0][0], len(list(g[1])))

    return [make_group(g) for g in itertools.groupby(s)]

if __name__ == '__main__':
    sample = "AAABBBCCD"
    result = run_length_encode(sample)
    print(result)