from itertools import groupby

def run_length_encode(data):
    if not data:
        return ()
    encoded = []
    for key, group in groupby(data):
        count = sum(1 for _ in group)
        encoded.append((key, count))
    return tuple(encoded)

if __name__ == '__main__':
    sample_input = "AAAABBBCCDA"
    result = run_length_encode(sample_input)
    print(result)