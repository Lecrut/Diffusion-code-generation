def run_length_encode(s):
    if not s:
        return []
    return [(char, sum(1 for _ in group)) for char, group in __import__('itertools').groupby(s)]

if __name__ == '__main__':
    print(run_length_encode("aaabbc"))