from itertools import groupby

def run_length_encode(data):
    return [(char, len(list(group))) for char, group in groupby(data)]

if __name__ == '__main__':
    sample_input = "aaabbccccdd"
    result = run_length_encode(sample_input)
    print(result)