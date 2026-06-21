from itertools import groupby

def aggregate_values(data):
    sorted_data = sorted(data)
    aggregated = {}
    for key, group in groupby(sorted_data, key=lambda x: x[0]):
        values = [item[1] for item in group]
        aggregated[key] = sum(values)
    return aggregated

if __name__ == '__main__':
    sample_data = [(3, 5), (1, 2), (3, 4), (1, 6), (2, 3)]
    result = aggregate_values(sample_data)
    print(result)