from itertools import groupby

def run_length_encode(data):
    return [(k, len(list(g))) for k, g in groupby(data)]

if __name__ == '__main__':
    sample_data = [1, 1, 2, 3, 3, 3, 4]
    result = run_length_encode(sample_data)
    print(result)