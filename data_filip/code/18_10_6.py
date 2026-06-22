from itertools import groupby

def run_length_encode(text):
    return [(char, len(list(group))) for char, group in groupby(text)]

if __name__ == '__main__':
    sample_input = "aaabbbaac"
    result = run_length_encode(sample_input)
    print(result)