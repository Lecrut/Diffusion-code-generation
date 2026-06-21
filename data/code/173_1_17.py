import itertools

def aggregate_values(data):
    sorted_data = sorted(data)
    result = {}
    for key, group in itertools.groupby(sorted_data, key=lambda x: x[0]):
        values = [item[1] for item in group]
        result[key] = sum(values)
    return result

if __name__ == '__main__':
    sample_data = [(3, 5), (1, 2), (3, 4), (2, 3), (1, 1)]
    print(aggregate_values(sample_data))