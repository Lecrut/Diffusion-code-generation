from itertools import groupby

def run_length_encode(data):
    return [(value, len(list(group))) for value, group in groupby(data)]

if __name__ == '__main__':
    values = [1, 1, 1, 2, 3, 3, 4, 4, 4, 4, 5]
    result = run_length_encode(values)
    print(result)