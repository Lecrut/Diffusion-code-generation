from itertools import groupby

def run_length_encode(data):
    if not data:
        return []
    return [(key, len(list(group))) for key, group in groupby(data)]

if __name__ == '__main__':
    sample_data = [1, 1, 1, 2, 2, 3, 3, 3, 3, 5, 5, 5, 5, 5]
    print(run_length_encode(sample_data))