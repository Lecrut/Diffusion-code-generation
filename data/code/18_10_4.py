import itertools

def run_length_encode(s):
    return [(char, len(list(group))) for char, group in itertools.groupby(s)]

if __name__ == '__main__':
    sample_string = "aaabbccccdde"
    result = run_length_encode(sample_string)
    print(result)