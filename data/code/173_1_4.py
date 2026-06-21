from itertools import groupby

def aggregate_values(data):
    sorted_data = sorted(data)
    aggregated = {key: sum((value for _, value in group)) for key, group in groupby(sorted_data, key=lambda x: x[0])}
    return aggregated
if __name__ == '__main__':
    sample_data = [(1, 2), (3, 4), (1, 6), (3, 8), (5, 10)]
    result = aggregate_values(sample_data)
    print(result)