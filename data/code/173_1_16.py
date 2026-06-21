from itertools import groupby

def aggregate_values(data):
    sorted_data = sorted(data)
    aggregated = {key: sum(values) for key, values in groupby(sorted_data, lambda x: x[0])}
    return aggregated

if __name__ == '__main__':
    sample_data = [(4, 1), (2, 3), (4, 5), (2, 7), (1, 9)]
    result = aggregate_values(sample_data)
    print(result)