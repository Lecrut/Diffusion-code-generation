from itertools import groupby

def run_length_encode(data):
    return [(len(list(group)), key) for key, group in groupby(data)]

if __name__ == '__main__':
    sample_input = "aaabbccccdd"
    result = run_length_encode(sample_input)
    print(result)