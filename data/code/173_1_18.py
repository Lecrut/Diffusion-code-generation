from itertools import groupby

def aggregate_values(data):
    sorted_data = sorted(data, key=lambda x: x[0])
    result = {}
    for key, group in groupby(sorted_data, key=lambda x: x[0]):
        values = [item[1] for item in group]
        result[key] = sum(values)
    return result

if __name__ == '__main__':
    sample_data = [(3, 5), (1, 2), (3, 4), (1, 6), (2, 3)]
    print(aggregate_values(sample_data))