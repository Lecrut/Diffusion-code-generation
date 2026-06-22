from itertools import groupby

def run_length_encode(data):
    return tuple((key, len(list(group))) for key, group in groupby(data))

if __name__ == '__main__':
    sample_input = 'AAAABBBCCDAABBB'
    result = run_length_encode(sample_input)
    print(result)