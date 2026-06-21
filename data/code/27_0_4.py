def run_length_encode(data):
    if not data:
        return []
    return [(char, sum(1 for _ in group)) for char, group in __import__('itertools').groupby(data)]

if __name__ == '__main__':
    print(run_length_encode('aabcccccaaa'))