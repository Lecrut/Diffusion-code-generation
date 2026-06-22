from itertools import groupby

def run_length_encode(s):
    return [(char, len(list(group))) for char, group in groupby(s)]

if __name__ == '__main__':
    sample_string = "aaabbccccde"
    result = run_length_encode(sample_string)
    print(result)