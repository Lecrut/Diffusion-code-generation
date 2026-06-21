from itertools import groupby

def validate_data(data):
    if not all(isinstance(item, tuple) and len(item) == 2 for item in data):
        raise ValueError("Data must be a list of tuples with exactly two elements")

def aggregate_values(data):
    validate_data(data)
    sorted_data = sorted(data)
    result = {}
    for key, group in groupby(sorted_data, key=lambda x: x[0]):
        values = [item[1] for item in group]
        result[key] = sum(values)
    return result

if __name__ == '__main__':
    sample_data = [(3, 5), (1, 2), (3, 4), (1, 6), (2, 3)]
    result = aggregate_values(sample_data)
    print(result)