from itertools import groupby

def aggregate_values(data):
    sorted_data = sorted(data, key=lambda x: x[0])
    aggregated = {key: sum(value for _, value in group) for key, group in groupby(sorted_data, key=lambda x: x[0])}
    return aggregated

if __name__ == '__main__':
    sample_data = [(1, 2), (3, 4), (1, 5), (3, 6), (2, 7)]
    result = aggregate_values(sample_data)
    print(result)