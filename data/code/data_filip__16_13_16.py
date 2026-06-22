from itertools import groupby

def run_length_encode(data):
    return [(key, len(list(group))) for key, group in groupby(data)]

if __name__ == '__main__':
    sample_data = [1, 1, 1, 2, 2, 3, 3, 3, 3, 5]
    result = run_length_encode(sample_data)
    print(result)