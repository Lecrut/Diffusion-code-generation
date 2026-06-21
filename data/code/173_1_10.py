from itertools import groupby

def aggregate_values(data):
    sorted_data = sorted(data)
    aggregated = {key: sum(values) for key, values in groupby(sorted_data, key=lambda x: x[0])}
    return aggregated
if __name__ == '__main__':
    sample_data = [(1, 2), (3, 4), (1, 5), (3, 6), (2, 7)]
    result = aggregate_values(sample_data)
    print(result)