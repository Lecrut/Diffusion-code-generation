from itertools import groupby

def run_length_encoding(data):
    result = []
    for key, group in groupby(data):
        count = sum(1 for _ in group)
        result.append((key, count))
    return result

if __name__ == '__main__':
    sample_data = [1, 1, 1, 2, 3, 3, 2, 2, 2, 1]
    print(run_length_encoding(sample_data))