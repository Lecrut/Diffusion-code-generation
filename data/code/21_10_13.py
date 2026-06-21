import itertools

def run_length_encode(data):
    if not data:
        return []
    return [(char, len(list(group))) for char, group in itertools.groupby(data)]

if __name__ == '__main__':
    sample_input = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
    result = run_length_encode(sample_input)
    print(result)