from itertools import groupby

def run_length_encoding(data):
    return [(key, len(list(group))) for key, group in groupby(data)]

if __name__ == '__main__':
    sample_string = "aaabbccccddee"
    result = run_length_encoding(sample_string)
    print(result)