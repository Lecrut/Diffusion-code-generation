import itertools

def run_length_encode(s):
    if not s:
        return []
    encoded = []
    for char, group in itertools.groupby(s):
        count = sum(1 for _ in group)
        encoded.append((char, count))
    return encoded

if __name__ == '__main__':
    sample_input = "aaabbccccdddd"
    result = run_length_encode(sample_input)
    print(result)