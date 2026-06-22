import itertools

def run_length_encode(data):
    return [(char, len(list(group))) for char, group in itertools.groupby(data)]

if __name__ == '__main__':
    sample_string = "aaabbccccddee"
    result = run_length_encode(sample_string)
    print(result)